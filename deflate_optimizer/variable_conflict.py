from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Tuple, Set, Optional, Iterable, Union
import ast
import io
import re
import tokenize

from .enumerate_variable_occurrences import list_var_occurrences, RESERVED

# ========= 出力データ構造 =========

@dataclass
class ConflictReport:
    names: List[str]                 # list_var_occurrences と同順
    conflict: List[List[bool]]       # N×N 対称ブール行列
    reason: List[List[Optional[str]]]# 同寸法 理由タグ

# ========= ユーティリティ =========

def _prefix_offsets(src: str):
    lines = src.splitlines(keepends=True)
    pref = [0]
    s = 0
    for ln in lines:
        s += len(ln)
        pref.append(s)
    def to_abs(lineno: int, col: int) -> int:
        return pref[lineno-1] + col
    return to_abs, lines

# list_var_occurrences(as_text=True) のテキストをリスト形式へ
def _parse_occurrences_text(text: str) -> List[Dict[str, List[int]]]:
    lines = text.splitlines()
    if not lines:
        return []
    try:
        n = int(lines[0].strip())
    except Exception as e:
        raise ValueError("occ_result text header is invalid") from e
    idx = 1
    out: List[Dict[str, List[int]]] = []
    for _ in range(n):
        if idx >= len(lines):
            raise ValueError("occ_result text is truncated at name line")
        name_count = lines[idx].rstrip("\n")
        idx += 1
        try:
            name, cnt_s = name_count.split(" ", 1)
            k = int(cnt_s)
        except Exception as e:
            raise ValueError(f"invalid name line: {name_count!r}") from e
        if idx >= len(lines):
            raise ValueError("occ_result text is truncated at positions line")
        pos_line = lines[idx].strip()
        idx += 1
        occs = [int(x) for x in pos_line.split()] if k and pos_line else []
        out.append({"name": name, "occurrences": occs})
    return out

# 文字列トークンの内容開始相対位置
_STR_HEAD_RE = re.compile(r"""(?ix)
    (?:[rubf]{0,3})
    ('''|\"\"\"|'|")
""")

def _string_content_head(token_src: str) -> int:
    m = _STR_HEAD_RE.match(token_src)
    return 0 if not m else len(m.group(0))

def _string_tail_len(token_src: str, content_rel: int) -> int:
    q3 = token_src[content_rel-3:content_rel]
    if q3 in ("'''", '"""'):
        return 3
    q1 = token_src[content_rel-1:content_rel]
    return 1 if q1 in ("'", '"') else 0

def _iter_str_consts_in_expr(src: str, expr: ast.AST) -> Iterable[Tuple[int, int]]:
    """
    引数式中に含まれる全ての文字列リテラルの内容部範囲を絶対オフセットで列挙
    """
    to_abs, _ = _prefix_offsets(src)
    for node in ast.walk(expr):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            seg = ast.get_source_segment(src, node)
            if seg is None:
                continue
            token_abs = to_abs(node.lineno, node.col_offset)
            head = _string_content_head(seg)
            tail = _string_tail_len(seg, head)
            a = token_abs + head
            b = token_abs + len(seg) - tail
            if a <= b:
                yield a, b

def _func_name(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None

# ========= メタ情報収集 =========

class _Meta:
    def __init__(self):
        # 位置集合
        self.ast_name_offsets: Set[int] = set()
        self.kwlabel_offsets: Set[int] = set()
        self.call_labels: Dict[int, Set[str]] = {}
        self.call_label_offsets: Dict[int, Set[int]] = {}

        # スコープ
        self.parent: Dict[int, Optional[int]] = {}
        self.kind: Dict[int, str] = {}
        self.scope_stack: List[int] = []
        self.next_scope_id = 0

        # 名に結びつく束縛と参照
        self.binds: Dict[str, Set[Tuple[int, str]]] = {}
        self.uses:  Dict[str, Set[int]] = {}
        self.import_scopes: Dict[str, Set[int]] = {}
        self.param_scopes: Dict[int, Set[str]] = {}
        self.func_class_binds_scopes: Dict[int, Set[str]] = {}
        self.del_scopes: Dict[str, Set[int]] = {}
        self.use_offsets: Dict[str, Set[int]] = {}

        # 文字列スパン
        self.string_spans: List[Tuple[int, int]] = []
        self.exec_content_spans: List[Tuple[int, int]] = []
        self.regex_content_spans: List[Tuple[int, int]] = []
        self.regex_group_names_by_span: Dict[int, Set[str]] = {}

def _new_scope(meta: _Meta, kind: str, parent: Optional[int]) -> int:
    sid = meta.next_scope_id
    meta.next_scope_id += 1
    meta.parent[sid] = parent
    meta.kind[sid] = kind
    return sid

def _is_ancestor(meta: _Meta, anc: int, desc: int) -> bool:
    cur = desc
    while cur is not None:
        if cur == anc:
            return True
        cur = meta.parent.get(cur)
    return False

def _collect_meta(src: str) -> _Meta:
    meta = _Meta()
    to_abs, lines = _prefix_offsets(src)
    tree = ast.parse(src)

    # 文字列トークンの全スパン
    reader = io.StringIO(src)
    for tok in tokenize.generate_tokens(reader.readline):
        if tok.type == tokenize.STRING:
            a = to_abs(tok.start[0], tok.start[1])
            b = to_abs(tok.end[0], tok.end[1])
            meta.string_spans.append((a, b))

    # スコープ管理
    def push(kind: str):
        parent = meta.scope_stack[-1] if meta.scope_stack else None
        sid = _new_scope(meta, kind, parent)
        meta.scope_stack.append(sid)
        return sid
    def pop():
        meta.scope_stack.pop()
    push("module")

    class V(ast.NodeVisitor):
        def cur(self) -> int:
            return meta.scope_stack[-1]

        def _bind_name(self, name: str, kind: str):
            meta.binds.setdefault(name, set()).add((self.cur(), kind))
            if kind in {"BindFunc", "BindClass"}:
                meta.func_class_binds_scopes.setdefault(self.cur(), set()).add(name)
        def _use_name(self, name: str):
            meta.uses.setdefault(name, set()).add(self.cur())

        def visit_NamedExpr(self, n: ast.NamedExpr):
            if isinstance(n.target, ast.Name):
                self._bind_name(n.target.id, "BindVar")
            self.generic_visit(n)

        def visit_Name(self, n: ast.Name):
            meta.ast_name_offsets.add(to_abs(n.lineno, n.col_offset))
            if isinstance(n.ctx, ast.Load):
                self._use_name(n.id)
                meta.use_offsets.setdefault(n.id, set()).add(to_abs(n.lineno, n.col_offset))
            elif isinstance(n.ctx, ast.Del):
                meta.del_scopes.setdefault(n.id, set()).add(self.cur())
            self.generic_visit(n)

        def visit_arg(self, a: ast.arg):
            meta.ast_name_offsets.add(to_abs(a.lineno, a.col_offset))
            self._bind_name(a.arg, "BindParam")
            meta.param_scopes.setdefault(self.cur(), set()).add(a.arg)

        def visit_FunctionDef(self, f: ast.FunctionDef):
            line = lines[f.lineno-1] if 1 <= f.lineno <= len(lines) else ""
            m = re.search(rf"\b({re.escape(f.name)})\s*(?=\()", line)
            if m:
                meta.ast_name_offsets.add(to_abs(f.lineno, m.start(1)))
            self._bind_name(f.name, "BindFunc")
            push("function"); self.generic_visit(f); pop()

        def visit_AsyncFunctionDef(self, f: ast.AsyncFunctionDef):
            self.visit_FunctionDef(f)

        def visit_ClassDef(self, c: ast.ClassDef):
            self._bind_name(c.name, "BindClass")
            push("class"); self.generic_visit(c); pop()

        def visit_Assign(self, n: ast.Assign):
            for t in n.targets:
                for name in _iter_store_names(t):
                    self._bind_name(name, "BindVar")
            self.generic_visit(n)

        def visit_AnnAssign(self, n: ast.AnnAssign):
            if isinstance(n.target, ast.Name):
                self._bind_name(n.target.id, "BindVar")
            self.generic_visit(n)

        def visit_AugAssign(self, n: ast.AugAssign):
            if isinstance(n.target, ast.Name):
                self._bind_name(n.target.id, "BindVar")
            self.generic_visit(n)

        def visit_For(self, n: ast.For):
            for name in _iter_store_names(n.target):
                self._bind_name(name, "BindVar")
            self.generic_visit(n)

        def visit_AsyncFor(self, n: ast.AsyncFor):
            self.visit_For(n)

        def visit_With(self, n: ast.With):
            for it in n.items:
                if it.optional_vars is not None:
                    for name in _iter_store_names(it.optional_vars):
                        self._bind_name(name, "BindVar")
            self.generic_visit(n)

        def visit_AsyncWith(self, n: ast.AsyncWith):
            self.visit_With(n)

        def visit_ExceptHandler(self, n: ast.ExceptHandler):
            if n.name:
                self._bind_name(n.name, "BindVar")
            self.generic_visit(n)

        def visit_Import(self, n: ast.Import):
            for a in n.names:
                nm = a.asname or a.name.split(".")[0]
                self._bind_name(nm, "BindImport")
                meta.import_scopes.setdefault(nm, set()).add(self.cur())

        def visit_ImportFrom(self, n: ast.ImportFrom):
            for a in n.names:
                nm = a.asname or a.name
                self._bind_name(nm, "BindImport")
                meta.import_scopes.setdefault(nm, set()).add(self.cur())

        def visit_ListComp(self, n: ast.ListComp):
            push("comp")
            for gen in n.generators:
                for name in _iter_store_names(gen.target):
                    self._bind_name(name, "BindComp")
            self.generic_visit(n); pop()

        def visit_SetComp(self, n: ast.SetComp):
            self.visit_ListComp(n)

        def visit_DictComp(self, n: ast.DictComp):
            self.visit_ListComp(n)

        def visit_GeneratorExp(self, n: ast.GeneratorExp):
            self.visit_ListComp(n)

        def visit_Lambda(self, n: ast.Lambda):
            push("lambda")
            for a in _iter_args(n.args):
                meta.ast_name_offsets.add(to_abs(a.lineno, a.col_offset))
                self._bind_name(a.arg, "BindParam")
                meta.param_scopes.setdefault(self.cur(), set()).add(a.arg)
            self.generic_visit(n); pop()

        def visit_Call(self, c: ast.Call):
            call_id = id(c)
            self._collect_kwlabel_positions(c, call_id)
            if isinstance(c.func, ast.Name) and c.func.id == "exec" and c.args:
                for a, b in _iter_str_consts_in_expr(src, c.args[0]):
                    meta.exec_content_spans.append((a, b))
            fun_name = _func_name(c.func)
            if fun_name is not None and fun_name in {
                "compile","search","match","fullmatch","sub","subn","finditer","findall","split"
            } and c.args:
                for a, b in _iter_str_consts_in_expr(src, c.args[0]):
                    meta.regex_content_spans.append((a, b))
            self.generic_visit(c)

        def _collect_kwlabel_positions(self, c: ast.Call, call_id: int):
            if not c.keywords:
                return
            to_abs_, _ = _prefix_offsets(src)
            call_abs_start = to_abs_(c.lineno, c.col_offset)
            labels: Set[str] = set()
            offset_set: Set[int] = set()
            for kw in c.keywords:
                if kw.arg is None:
                    continue
                labels.add(kw.arg)
                val_abs = to_abs_(kw.value.lineno, kw.value.col_offset)
                seg = src[call_abs_start:val_abs]
                m_last = None
                for m in re.finditer(rf"\b({re.escape(kw.arg)})\s*=", seg):
                    m_last = m
                if m_last:
                    off = call_abs_start + m_last.start(1)
                    meta.kwlabel_offsets.add(off)
                    offset_set.add(off)
            if labels:
                meta.call_labels[call_id] = labels
                meta.call_label_offsets[call_id] = offset_set

    V().visit(tree)
    meta.scope_stack.clear()
    return meta

def _iter_store_names(target: ast.AST) -> Iterable[str]:
    if isinstance(target, ast.Name):
        yield target.id
    elif isinstance(target, (ast.Tuple, ast.List)):
        for elt in target.elts:
            yield from _iter_store_names(elt)
    elif isinstance(target, ast.Starred):
        yield from _iter_store_names(target.value)

def _iter_args(args: ast.arguments) -> Iterable[ast.arg]:
    for a in args.posonlyargs + args.args + args.kwonlyargs:
        yield a
    if args.vararg:
        yield args.vararg
    if args.kwarg:
        yield args.kwarg

def _pos_in_any(p: int, spans: List[Tuple[int, int]]) -> bool:
    return any(a <= p < b for a, b in spans)

def _pos_bucket_ids(p: int, spans: List[Tuple[int, int]]) -> Set[int]:
    out = set()
    for i, (a, b) in enumerate(spans):
        if a <= p < b:
            out.add(i)
    return out

# ========= 名ごとの特徴量を構築 =========

@dataclass
class _NameInfo:
    name: str
    occs: List[int]
    is_upper: bool
    kinds: Set[str]                    # "AST_NAME" "KW_LABEL" "IN_EXEC_STR" "IN_REGEX_STR" "IN_OTHER_STR" など
    exec_span_ids: Set[int]
    regex_span_ids: Set[int]
    bind_scopes: Set[int]
    bind_kinds: Set[str]
    import_scopes: Set[int]
    use_scopes: Set[int]
    del_scopes: Set[int]
    label_call_ids: Set[int]

def _build_name_infos(src: str, occ_result: List[Dict], meta: _Meta) -> Dict[str, _NameInfo]:
    ast_pos = meta.ast_name_offsets
    kw_pos = meta.kwlabel_offsets
    str_spans = meta.string_spans
    exec_spans = meta.exec_content_spans
    regex_spans = meta.regex_content_spans

    label_call_ids_by_name: Dict[str, Set[int]] = {}
    for cid, labels in meta.call_labels.items():
        for nm in labels:
            label_call_ids_by_name.setdefault(nm, set()).add(cid)

    infos: Dict[str, _NameInfo] = {}
    for item in occ_result:
        nm = item["name"]
        occs = item.get("occurrences", [])
        kinds: Set[str] = set()
        exec_ids: Set[int] = set()
        regex_ids: Set[int] = set()
        for p in occs:
            if p in ast_pos:
                kinds.add("AST_NAME")
            elif p in kw_pos:
                kinds.add("KW_LABEL")
            else:
                in_exec = _pos_bucket_ids(p, exec_spans)
                in_regex = _pos_bucket_ids(p, regex_spans)
                if in_exec:
                    kinds.add("IN_EXEC_STR"); exec_ids |= in_exec
                elif in_regex:
                    kinds.add("IN_REGEX_STR"); regex_ids |= in_regex
                elif _pos_in_any(p, str_spans):
                    kinds.add("IN_OTHER_STR")
                else:
                    kinds.add("OTHER")

        infos[nm] = _NameInfo(
            name=nm,
            occs=occs,
            is_upper=nm.isupper(),
            kinds=kinds,
            exec_span_ids=exec_ids,
            regex_span_ids=regex_ids,
            bind_scopes={s for s, _ in meta.binds.get(nm, set())},
            bind_kinds={k for _, k in meta.binds.get(nm, set())},
            import_scopes=meta.import_scopes.get(nm, set()),
            use_scopes=meta.uses.get(nm, set()),
            del_scopes=meta.del_scopes.get(nm, set()),
            label_call_ids=label_call_ids_by_name.get(nm, set()),
        )
    return infos

# ========= 衝突判定規則 =========

def _mark(conflict: List[List[bool]], reason: List[List[Optional[str]]], i: int, j: int, why: str):
    conflict[i][j] = conflict[j][i] = True
    reason[i][j] = reason[j][i] = why

def _used_under_scope(meta: _Meta, name: str, scope_id: int) -> bool:
    for s in meta.uses.get(name, set()):
        if _is_ancestor(meta, scope_id, s):
            return True
    return False

def _build_conflicts_with_rules(names: List[str], infos: Dict[str, _NameInfo], meta: _Meta) -> ConflictReport:
    N = len(names)
    conflict = [[False]*N for _ in range(N)]
    reason   = [[None]*N for _ in range(N)]

    def has(info: _NameInfo, k: str) -> bool:
        return k in info.kinds

    func_param_scopes = meta.param_scopes
    for i in range(N):
        for j in range(i+1, N):
            ni, nj = names[i], names[j]
            Ii, Ij = infos.get(ni), infos.get(nj)
            if Ii is None or Ij is None:
                continue

            # U4 同一呼び出し内のキーワードラベル重複
            if Ii.label_call_ids & Ij.label_call_ids:
                _mark(conflict, reason, i, j, "U4:kw-label-dup")
                continue

            # R1a 同一関数スコープでの引数名重複
            for sid, params in func_param_scopes.items():
                if ni in params and nj in params:
                    _mark(conflict, reason, i, j, "R1a:param-dup")
                    break
            if conflict[i][j]:
                continue

            # R1c 同一スコープの関数名またはクラス名重複
            for sid, defs in meta.func_class_binds_scopes.items():
                if ni in defs and nj in defs:
                    _mark(conflict, reason, i, j, "R1c:def-dup")
                    break
            if conflict[i][j]:
                continue

            # R2 シャドーイング 使用実体がある場合のみ
            r2_hit = False
            for s_in in Ii.bind_scopes:
                for s_out in Ij.bind_scopes:
                    if _is_ancestor(meta, s_out, s_in) and _used_under_scope(meta, nj, s_in):
                        r2_hit = True; break
                if r2_hit: break
            if not r2_hit:
                for s_in in Ij.bind_scopes:
                    for s_out in Ii.bind_scopes:
                        if _is_ancestor(meta, s_out, s_in) and _used_under_scope(meta, ni, s_in):
                            r2_hit = True; break
                    if r2_hit: break
            if r2_hit:
                _mark(conflict, reason, i, j, "R2:shadowing")
                continue

            # R3 import 名との衝突 使用実体ありかつスコープ干渉時のみ
            if Ii.import_scopes or Ij.import_scopes:
                r3_hit = False
                if Ii.import_scopes:
                    for s_out in Ii.import_scopes:
                        for s_in in Ij.bind_scopes or Ij.use_scopes:
                            if _is_ancestor(meta, s_out, s_in) and _used_under_scope(meta, ni, s_in):
                                r3_hit = True; break
                        if r3_hit: break
                if not r3_hit and Ij.import_scopes:
                    for s_out in Ij.import_scopes:
                        for s_in in Ii.bind_scopes or Ii.use_scopes:
                            if _is_ancestor(meta, s_out, s_in) and _used_under_scope(meta, nj, s_in):
                                r3_hit = True; break
                        if r3_hit: break
                if r3_hit:
                    _mark(conflict, reason, i, j, "R3:import-collision")
                    continue

            # R6 del と束縛の干渉 祖先関係かつ使用実体あり
            r6_hit = False
            for sdel in Ii.del_scopes:
                for sb in Ij.bind_scopes or Ij.use_scopes:
                    if _is_ancestor(meta, sdel, sb) and (_used_under_scope(meta, nj, sb) or Ij.bind_scopes):
                        r6_hit = True; break
                if r6_hit: break
            if not r6_hit:
                for sdel in Ij.del_scopes:
                    for sb in Ii.bind_scopes or Ii.use_scopes:
                        if _is_ancestor(meta, sdel, sb) and (_used_under_scope(meta, ni, sb) or Ii.bind_scopes):
                            r6_hit = True; break
                    if r6_hit: break
            if r6_hit:
                _mark(conflict, reason, i, j, "R6:del-interfere")
                continue

            # U1 文字列内大文字と AST 名の合一 対象は exec と正規表現のみ
            if Ii.is_upper and (has(Ii, "IN_EXEC_STR") or has(Ii, "IN_REGEX_STR")) and \
               (has(Ij, "AST_NAME") or Ij.bind_scopes or Ij.use_scopes):
                _mark(conflict, reason, i, j, "U1:upper-string-vs-ast")
                continue
            if Ij.is_upper and (has(Ij, "IN_EXEC_STR") or has(Ij, "IN_REGEX_STR")) and \
               (has(Ii, "AST_NAME") or Ii.bind_scopes or Ii.use_scopes):
                _mark(conflict, reason, i, j, "U1:upper-string-vs-ast")
                continue

            # U2 同一 exec 文字列内の大文字どうし
            if Ii.is_upper and Ij.is_upper and Ii.exec_span_ids & Ij.exec_span_ids:
                _mark(conflict, reason, i, j, "U2:same-exec-string")
                continue

            # U3 同一正規表現内のグループ名重複
            if Ii.is_upper and Ij.is_upper:
                for span_id, names_in_span in _regex_group_names_by_span(meta).items():
                    if names[i] in names_in_span and names[j] in names_in_span:
                        _mark(conflict, reason, i, j, "U3:regex-group-dup")
                        break
                if conflict[i][j]:
                    continue

            # R1d 簡易データフロー干渉 参照が存在する場合のみ
            if "BindVar" in Ii.bind_kinds and "BindVar" in Ij.bind_kinds and \
               (Ii.bind_scopes & Ij.bind_scopes) and (Ii.use_scopes or Ij.use_scopes):
                _mark(conflict, reason, i, j, "R1d:dataflow-approx")
                continue

            # R1e 同一スコープで引数と代入が合一
            same_scope_param_var = any(
                (sid in meta.param_scopes and ni in meta.param_scopes[sid] and sid in Ij.bind_scopes and "BindVar" in Ij.bind_kinds) or
                (sid in meta.param_scopes and nj in meta.param_scopes[sid] and sid in Ii.bind_scopes and "BindVar" in Ii.bind_kinds)
                for sid in set(Ii.bind_scopes) | set(Ij.bind_scopes) | set(meta.param_scopes.keys())
            )
            if same_scope_param_var:
                _mark(conflict, reason, i, j, "R1e:param-vs-var")
                continue

    return ConflictReport(names=names, conflict=conflict, reason=reason)

def _regex_group_names_by_span(meta: _Meta) -> Dict[int, Set[str]]:
    # 呼び出し側で上書きされるプレースホルダ
    return {}

# ========= パブリック関数 =========

def build_conflict_report(src: str,
                          occ_result: Union[str, List[Dict]],
                          *,
                          assume_preprocessed: bool = True,
                          as_text: bool = False) -> ConflictReport | str:
    """
    src は list_var_occurrences でオフセットを算出したソースと同一であること
    occ_result はリストまたはテキスト形式のいずれでもよい
    as_text が真のときは行列のみを返す
    """
    if isinstance(src, bytes):
        src = src.decode("utf-8", errors="replace")

    if isinstance(occ_result, str):
        occ_list = _parse_occurrences_text(occ_result)
    else:
        occ_list = occ_result

    meta = _collect_meta(src)

    # 正規表現グループ名の抽出
    regex_names_by_span: Dict[int, Set[str]] = {}
    for span_id, (a, b) in enumerate(meta.regex_content_spans):
        s = src[a:b]
        names_in_span: Set[str] = set()
        for m in re.finditer(r"\(\?P<([A-Za-z_][A-Za-z_0-9]*)>", s):
            names_in_span.add(m.group(1))
        for m in re.finditer(r"\\g<([A-Za-z_][A-Za-z_0-9]*)>", s):
            names_in_span.add(m.group(1))
        regex_names_by_span[span_id] = names_in_span

    def _regex_group_names_by_span_bound(_meta: _Meta = meta,
                                         _cache: Dict[int, Set[str]] = regex_names_by_span):
        return _cache
    globals()["_regex_group_names_by_span"] = _regex_group_names_by_span_bound

    infos = _build_name_infos(src, occ_list, meta)
    names = [item["name"] for item in occ_list]

    report = _build_conflicts_with_rules(names, infos, meta)

    if as_text:
        rows = []
        n = len(report.names)
        for i in range(n):
            rows.append(" ".join("1" if report.conflict[i][j] else "0" for j in range(n)))
        return "\n".join(rows)

    return report

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} source.py [--matrix]", file=sys.stderr)
        sys.exit(2)

    matrix_only = "--matrix" in sys.argv[1:]
    path = next(a for a in sys.argv[1:] if a != "--matrix")

    with open(path, "r", encoding="utf-8") as f:
        src = f.read()

    occ = list_var_occurrences(src)  # 既存関数
    out = build_conflict_report(src, occ, as_text=matrix_only)

    if matrix_only:
        print(out, end="")
    else:
        import json
        rep: ConflictReport = out  # type: ignore
        print(json.dumps({
            "names": rep.names,
            "conflict": rep.conflict,
            "reason": rep.reason,
        }, ensure_ascii=False, indent=2))
