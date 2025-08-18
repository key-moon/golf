# best: 94
# 9x9グリッド 背景: 0
# 要素が{1,8}の 3x3のグリッドが4つ
# 8が一番少ない or 1 が一番多いグリッドを抽出
# p=lambda g:eval(max((a.count("1"),a) for x in range(49) if "0" not in (a:=str([r[x%7:][:3]for r in g[x//7:][:3]])))[1])
# p=lambda g:eval(max((a.count("1"),a) for x in range(49) if "0"not in(a:=str([r[x%7:][:3]for r in g[x//7:][:3]])))[1])
# アイデア: zip(g,g[1:],g[2:]) みたいなことすると伸びるかも
# p=lambda g:max((str(a).count('1'),a)for x in range(49)if 0<min(min(a:=[r[x%7:][:3]for r in g[x//7:][:3]])))[1]
# p=lambda g:min((sum(sum(a,[])),a)for x in range(49)if 0<min(min(a:=[r[x%7:][:3]for r in g[x//7:][:3]])))[1]
# p=lambda g:min((sum(sum(a,[])),a)for x in range(49)if 0<min(min(a:=[r[x%7:][:3]for r in g[x//7:][:3]])))[1]
# ============================================================================================
p=lambda g:min((sum(sum(a,[])),a)for x in range(49)if 0<min(min(a:=[r[x%7:][:3]for r in g[x//7:][:3]])))[1]
