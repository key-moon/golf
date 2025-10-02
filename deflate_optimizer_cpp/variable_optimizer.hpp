#pragma once
#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"
#include "variable.hpp"
#include "xorshift.hpp"


struct CharStat {
    bool var_candidate = false;
    int num_var_occurrences_as_literal;
    int num_nonvar_occurrences_as_literal;
    int num_var_occurrences_as_nonliteral;
    int num_nonvar_occurrencess_as_nonliteral;
    int lit_code_length;
};

bool is_p_replaceable(DynamicHuffmanBlock& block) {
    auto text = block.get_string({});
    text.emplace_back(0);
    // textから[a-zA-Z_]+ の変数を列挙して確認し、`p` の出現が一回のみならreplaceableとする

    auto is_literal_char = [](int c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || c == '_';
    };

    int p_occ = 0;
    std::vector<int> now_literal;
    for(auto c : text) {
        if (is_literal_char(c)) {
            now_literal.push_back(c);
        } else {
            if (now_literal.size() > 0) {
                if (now_literal.size() == 1 && now_literal[0] == 'p') {
                    if (++p_occ > 1) {
                        return false;
                    }
                }
                now_literal.clear();
            }
        }
    }
    return p_occ == 1;
}


std::vector<CharStat> get_char_stats(DynamicHuffmanBlock& block, const std::vector<Variable>& variables) {
    auto text = block.get_string({});
    std::vector<bool> is_lieral_position(text.size());
    std::vector<int> literal_freq(256, 0);
    std::vector<int> nonliteral_freq(256, 0);

    int ptr = 0;
    for (auto tok : block.tokens) {
        if (tok.type == Token::LITERAL) {
            is_lieral_position[ptr] = true;
            literal_freq[tok.literal]++;
            ptr += 1;
        } else { // COPY
            for (int i = 0; i < tok.pair.length; ++i) {
                nonliteral_freq[text[ptr + i]]++;
            }
            ptr += tok.pair.length;
        }
    }

    std::vector<int> num_lit_occurrences_of_vars(variables.size(), 0);
    std::vector<int> num_nonlit_occurrences_of_vars(variables.size(), 0);
    for (int i = 0; i < variables.size(); ++i) {
        for (auto pos : variables[i].occurrences) {
            for (int j = 0; j < variables[i].name.size(); ++j) {
                if (text[pos + j] != static_cast<int>(variables[i].name[j])) {
                    std::cerr << "Error: variable occurrence does not match variable name\n";
                    std::cerr << "Variable: " << variables[i].name << "\n";
                    std::cerr << "Occurrence at position " << pos << ": ";
                    for (int k = 0; k < variables[i].name.size(); ++k) {
                        std::cerr << static_cast<char>(text[pos + k]);
                    }
                    std::cerr << "\n";
                    exit(1);
                }
            }
            if (is_lieral_position[pos]) {
                num_lit_occurrences_of_vars[i]++;
            }
            else {
                num_nonlit_occurrences_of_vars[i]++;
            }
        }
    }
    std::vector<CharStat> char_stats(256);
    for (int i = 'A'; i <= 'Z'; ++i) char_stats[i].var_candidate = true;
    // 'p' が関数定義のみに使われているなら 'p' をshadowingしても良い
    for (int i = 'a'; i <= 'z'; ++i) if (i != 'p' || is_p_replaceable(block)) char_stats[i].var_candidate = true;
    char_stats['_'].var_candidate = true;

    for (int i = 0; i < 256; ++i) {
        char_stats[i].num_var_occurrences_as_literal = 0;
        char_stats[i].num_nonvar_occurrences_as_literal = literal_freq[i];
        char_stats[i].num_var_occurrences_as_nonliteral = 0;
        char_stats[i].num_nonvar_occurrencess_as_nonliteral = nonliteral_freq[i];
        char_stats[i].lit_code_length = block.literal_code_lengths[i];
    }

    for (int i = 0; i < variables.size(); ++i) {
        if (variables[i].name.size() != 1) continue;
        int char_val = static_cast<int>(variables[i].name[0]);
        if (!char_stats[char_val].var_candidate) continue;
        char_stats[char_val].num_var_occurrences_as_literal = num_lit_occurrences_of_vars[i];
        char_stats[char_val].num_nonvar_occurrences_as_literal -= num_lit_occurrences_of_vars[i];
        char_stats[char_val].num_var_occurrences_as_nonliteral = num_nonlit_occurrences_of_vars[i];
        char_stats[char_val].num_nonvar_occurrencess_as_nonliteral -= num_nonlit_occurrences_of_vars[i];
    }
    return char_stats;
}


void replace_and_recompute_parsing(DynamicHuffmanBlock& block, std::vector<Variable>& variables, const std::vector<int>& variable_to_new_literal_mapping) {
    auto text = block.get_string({});
    for (int i = 0; i < variables.size(); ++i) {
        if (variable_to_new_literal_mapping[i] == -1) continue;
        int new_val = variable_to_new_literal_mapping[i];
        variables[i].name = std::string(1, static_cast<char>(new_val));
        for(auto pos : variables[i].occurrences) {
            for (int j = 0; j < variables[i].name.size(); ++j) {
                text[pos + j] = new_val;
            }
        }
    }
    // 再度optimal parse
    block.tokens.clear();
    for(auto c : text) {
        block.tokens.push_back(Token{ .type = Token::LITERAL, .literal = static_cast<unsigned char>(c) });
    }
    block.tokens = optimal_parse_block(block, {});
}

enum FreqCount {
    NumNonVarAsLiteral,
    NumNonVarAll,
};

enum TieBreak {
    BFS,
    NonVarFreq,
    NoUpdate,
    RandomSwap,
    RandomSwapCL,
    ChangeVarSet,
};

enum VariableAssignment {
    Injective, // 複数出現をマージしない
    Greedy,    // 出現頻度順に割り当て先を決める 割り当て先は衝突が起こらないなかで優先度最大のもの
    DP,        // 出現頻度の偏りが最大（エントロピーが最小）になるようにDP
};

// 使用された文字の集合をrun-length encodedで保持し、その際の各runの端の文字を移動させる候補とする
// 移動先の文字は、non lit occが存在するがまだ割り当てられていない文字か、runの端を拡張した文字
std::vector<int> change_variable_set(DynamicHuffmanBlock& block, std::vector<Variable>& variables, const std::vector<std::vector<bool>>& conflict_mat) {
    auto text = block.get_string({});
    auto char_stats = get_char_stats(block, variables);

    std::vector<bool> used_chars(256, false);
    for (auto c : text) {
        used_chars[c] = true;
    }
    std::vector<std::pair<int,int>> runs; // (start, end)
    for (int i = 0; i < 256; ++i) {
        if (!used_chars[i]) continue;
        int j = i;
        while (j + 1 < 256 && used_chars[j + 1]) j++;
        runs.emplace_back(i, j);
        i = j;
    };
    std::vector<int> candidate_chars;
    for (auto [start, end] : runs) {
        if (start > 0 && char_stats[start].num_var_occurrences_as_literal + char_stats[start].num_var_occurrences_as_nonliteral > 0) {
            candidate_chars.push_back(start);
        }
        if (end + 1 < 256 && char_stats[end].num_var_occurrences_as_literal + char_stats[end].num_var_occurrences_as_nonliteral > 0) {
            candidate_chars.push_back(end);
        }
    }
    std::vector<int> replace_cand_chars;
    for (int i = 0; i < 256; ++i) {
        if (!char_stats[i].var_candidate) continue;
        if (char_stats[i].num_var_occurrences_as_literal + char_stats[i].num_var_occurrences_as_nonliteral > 0) continue;
        if (char_stats[i].num_nonvar_occurrences_as_literal + char_stats[i].num_nonvar_occurrencess_as_nonliteral == 0) continue;
        replace_cand_chars.push_back(i);
    }
    for (auto [start, end] : runs) {
        if (start > 0 && char_stats[start - 1].var_candidate) {
            replace_cand_chars.push_back(start - 1);
        }
        if (end + 1 < 256 && char_stats[end + 1].var_candidate) {
            replace_cand_chars.push_back(end + 1);
        }
    }
    std::sort(replace_cand_chars.begin(), replace_cand_chars.end());
    replace_cand_chars.erase(std::unique(replace_cand_chars.begin(), replace_cand_chars.end()), replace_cand_chars.end());

    XorShift::shuffle(candidate_chars);
    XorShift::shuffle(replace_cand_chars);
    int num_changes = std::min({(int)candidate_chars.size(), (int)replace_cand_chars.size(), 3});
    std::vector<int> variable_to_new_literal_mapping(variables.size(), -1);
    if (num_changes == 0) return variable_to_new_literal_mapping;

    num_changes = XorShift::randn(num_changes) + 1;
    std::vector<std::vector<int>> char_to_var_indices(256);
    for (int i = 0; i < variables.size(); ++i) {
        if (variables[i].name.size() != 1) continue;
        unsigned char c = static_cast<unsigned char>(variables[i].name[0]);
        char_to_var_indices[c].push_back(i);
    }
    for (int i = 0; i < num_changes; ++i) {
        int from_char = candidate_chars[i];
        int to_char = replace_cand_chars[i];
        if (from_char == to_char) {
            char_to_var_indices[from_char].clear();
            continue;
        }
        auto& indices = char_to_var_indices[from_char];
        if (indices.empty()) continue;
        for (int var_idx : indices) {
            variable_to_new_literal_mapping[var_idx] = to_char;
        }
        indices.clear();
    }
    return variable_to_new_literal_mapping;
}

// ビット数が少ないところに貪欲に当てはめていく
// ビット数が同じ場合、既に埋めたところに近いものを優先的に割り当てる感じで
// このアルゴリズムは適当に変えたりvariantを作ったりしていい
std::vector<int> optimize_variables(DynamicHuffmanBlock& block, std::vector<Variable>& variables, const std::vector<std::vector<bool>>& conflict_mat, FreqCount freq_count, TieBreak tie_break = TieBreak::BFS, VariableAssignment var_assign = VariableAssignment::Injective) {

    if (conflict_mat.empty() && var_assign != VariableAssignment::Injective) {
        std::cerr << "Error: Conflict matrix is empty, but variable assignment is not injective.\n";
        exit(1);
    }

    auto text = block.get_string({});
    auto char_stats = get_char_stats(block, variables);
    std::vector<int> replace_cand_vars; // 変数をliteralとしての出現回数でソート
    std::vector<int> variable_char_to_id(256, -1);
    for (int i = 0; i < variables.size(); ++i) {
        if (variables[i].name.size() != 1) continue;
        int char_val = static_cast<int>(variables[i].name[0]);
        variable_char_to_id[char_val] = i;
        if (!char_stats[char_val].var_candidate) continue;
        replace_cand_vars.push_back(i);
    }
    std::sort(replace_cand_vars.begin(), replace_cand_vars.end(), [&](int a, int b) {
        if (freq_count == FreqCount::NumNonVarAsLiteral) {
            return char_stats[static_cast<int>(variables[a].name[0])].num_var_occurrences_as_literal
                > char_stats[static_cast<int>(variables[b].name[0])].num_var_occurrences_as_literal;
        }
        else {
            return (char_stats[static_cast<int>(variables[a].name[0])].num_var_occurrences_as_literal
                + char_stats[static_cast<int>(variables[a].name[0])].num_var_occurrences_as_nonliteral)
                > (char_stats[static_cast<int>(variables[b].name[0])].num_var_occurrences_as_literal
                + char_stats[static_cast<int>(variables[b].name[0])].num_var_occurrences_as_nonliteral);
        }
    });

    std::vector<int> assigned_literal_code(variables.size(), -1);
    std::vector<bool> used_chars(256, false);

    std::vector<std::vector<int>> code_length_symbol_map(17);
    for (int i = 0; i < 256; ++i) {
        if (!char_stats[i].var_candidate) continue;
        code_length_symbol_map[char_stats[i].lit_code_length].push_back(i);
    }
    int ptr = 0;
    for (int len = 1; len <= 16; ++len) {
        if (code_length_symbol_map[len].size() == 0) continue;
        std::vector<int> traverse_vars_list;
        std::vector<int> distance_vec(256, 1e9);
        std::queue<int> que;

        if (tie_break == TieBreak::BFS) {
            if (ptr == 0) {
                // 最初の変数はlit codeの出現頻度で決める
                int max_elm = *std::max_element(code_length_symbol_map[len].begin(), code_length_symbol_map[len].end(), [&](int a, int b) {
                    if (freq_count == FreqCount::NumNonVarAsLiteral) {
                        return char_stats[a].num_nonvar_occurrences_as_literal < char_stats[b].num_nonvar_occurrences_as_literal;
                    }
                    else {
                        return (char_stats[a].num_nonvar_occurrences_as_literal + char_stats[a].num_nonvar_occurrencess_as_nonliteral)
                            < (char_stats[b].num_nonvar_occurrences_as_literal + char_stats[b].num_nonvar_occurrencess_as_nonliteral);
                    }
                });
                assigned_literal_code[ptr] = max_elm;
                used_chars[max_elm] = true;
                ++ptr;
            }

            for (int j = 0; j < 256; ++j) {
                if (used_chars[j]) {
                    distance_vec[j] = 0;
                    que.push(j);
                }
            }
            while (!que.empty()) {
                int v = que.front();
                que.pop();
                if (char_stats[v].lit_code_length == len && !used_chars[v] && char_stats[v].var_candidate) {
                    used_chars[v] = true;
                    traverse_vars_list.push_back(v);
                }
                for (int u : std::vector<int>{v + 1, v - 1}) {
                    if (u < 0 || u >= 256) continue;
                    if (distance_vec[u] > distance_vec[v] + 1) {
                        distance_vec[u] = distance_vec[v] + 1;
                        que.push(u);
                    }
                }
            }
            for(auto var : traverse_vars_list) {
                assigned_literal_code[ptr] = var;
                ++ptr;
                if (ptr >= replace_cand_vars.size()) break;
            }
        }
        else if (tie_break == TieBreak::NonVarFreq) {
            // lit codeの出現頻度で決める
            std::sort(code_length_symbol_map[len].begin(), code_length_symbol_map[len].end(), [&](int a, int b) {
                if (freq_count == FreqCount::NumNonVarAsLiteral) {
                    return char_stats[a].num_nonvar_occurrences_as_literal > char_stats[b].num_nonvar_occurrences_as_literal;
                }
                else {
                    return (char_stats[a].num_nonvar_occurrences_as_literal + char_stats[a].num_nonvar_occurrencess_as_nonliteral)
                        > (char_stats[b].num_nonvar_occurrences_as_literal + char_stats[b].num_nonvar_occurrencess_as_nonliteral);
                }
            });
            for(auto var : code_length_symbol_map[len]) {
                if (used_chars[var]) continue;
                assigned_literal_code[ptr] = var;
                used_chars[var] = true;
                ++ptr;
                if (ptr >= replace_cand_vars.size()) break;
            }
        }
        if (ptr >= replace_cand_vars.size()) break;
    }
    std::vector<int> variable_to_new_literal_mapping(variables.size(), -1);
    if (var_assign == VariableAssignment::Injective) {
        // 変数は単射で、出現のマージはしない
        ptr = 0;
        for(auto i : replace_cand_vars) {
            if (variables[i].name.size() != 1) continue;
            int char_val = static_cast<int>(variables[i].name[0]);
            int new_val = assigned_literal_code[ptr++];
            if (new_val == -1) {
                continue;
            }
            if (new_val == char_val) {
                continue;
            }
            variable_to_new_literal_mapping[i] = new_val;
        }
    }
    else if (var_assign == VariableAssignment::Greedy) {

        // 衝突しない変数名を、候補から貪欲に当てはめていく
        std::vector<std::vector<int>> assignmented_var_ids(256);
        for(auto i : replace_cand_vars) {
            if (variables[i].name.size() != 1) continue;
            int char_val = static_cast<int>(variables[i].name[0]);
            // 次の変数候補、衝突しているかもしれないのでチェック
            for  (auto new_val : assigned_literal_code) {
                if (new_val == -1) continue;
                bool fl = true;
                for (auto assigned_var_id : assignmented_var_ids[new_val]) {
                    if (conflict_mat[i][assigned_var_id] || conflict_mat[assigned_var_id][i]) {
                        fl = false;
                    }
                }
                if (!fl) continue;

                if (new_val == char_val) continue;
                variable_to_new_literal_mapping[i] = new_val;
                assignmented_var_ids[new_val].push_back(i);
                break;
            }
        }
    }

    return variable_to_new_literal_mapping;
}
