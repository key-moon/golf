#pragma once
#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"
#include "variable.hpp"


void optimize_variables(DynamicHuffmanBlock& block, std::vector<Variable>& variables, const std::vector<int>& context) {

    auto text = block.get_string(context);
    std::vector<bool> is_lieral_position(text.size());

    std::vector<int> literal_freq(256, 0);

    int ptr = 0;
    for (auto tok : block.tokens) {
        if (tok.type == Token::LITERAL) {
            is_lieral_position[ptr] = true;
            literal_freq[tok.literal]++;
            ptr += 1;
        } else { // COPY
            ptr += tok.pair.length;
        }
    }

    /*
    std::cerr << "=-------- Original String ---------\n";
    for(auto c : text) {
        std::cerr << static_cast<char>(c);
    }
    std::cerr << "\n\n";
    */

    std::vector<int> num_lit_occurrences_of_vars(variables.size(), 0);
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
        }
    }
    struct CharStat {
        bool var_candidate = false;
        int num_var_occurrences_as_literal;
        int num_nonvar_occurrences_as_literal;
        int lit_code_length;
    };
    std::vector<CharStat> char_stats(256);
    for (int i = 'A'; i <= 'Z'; ++i) char_stats[i].var_candidate = true;
    for (int i = 'a'; i <= 'z'; ++i) if (i != 'p') char_stats[i].var_candidate = true;
    char_stats['_'].var_candidate = true;

    for (int i = 0; i < 256; ++i) {
        char_stats[i].num_var_occurrences_as_literal = 0;
        char_stats[i].num_nonvar_occurrences_as_literal = literal_freq[i];
        char_stats[i].lit_code_length = block.literal_code_lengths[i];
    }

    for (int i = 0; i < variables.size(); ++i) {
        if (variables[i].name.size() != 1) continue;
        int char_val = static_cast<int>(variables[i].name[0]);
        if (!char_stats[char_val].var_candidate) continue;
        char_stats[char_val].num_var_occurrences_as_literal = num_lit_occurrences_of_vars[i];
        char_stats[char_val].num_nonvar_occurrences_as_literal -= num_lit_occurrences_of_vars[i];
    }

    // とりあえず、ビット数が少ないところに貪欲に当てはめていく
    // ビット数が同じ場合、既に埋めたところに近いものを優先的に割り当てる感じで
    std::vector<int> replace_cand_vars; // 変数をliteralとしての出現回数でソート
    for (int i = 0; i < variables.size(); ++i) {
        if (variables[i].name.size() != 1) continue;
        int char_val = static_cast<int>(variables[i].name[0]);
        if (!char_stats[char_val].var_candidate) continue;
        replace_cand_vars.push_back(i);
    }
    std::sort(replace_cand_vars.begin(), replace_cand_vars.end(), [&](int a, int b) {
        return char_stats[static_cast<int>(variables[a].name[0])].num_var_occurrences_as_literal
             > char_stats[static_cast<int>(variables[b].name[0])].num_var_occurrences_as_literal;
    });

    std::vector<int> assigned_literal_code(variables.size(), -1);
    std::vector<bool> used_chars(256, false);

    std::vector<std::vector<int>> code_length_symbol_map(17);
    for (int i = 0; i < 256; ++i) {
        if (!char_stats[i].var_candidate) continue;
        code_length_symbol_map[char_stats[i].lit_code_length].push_back(i);
    }
    ptr = 0;
    for (int len = 1; len <= 16; ++len) {
        if (code_length_symbol_map[len].size() == 0) continue;
        std::vector<int> traverse_vars_list;
        std::vector<int> distance_vec(256, 1e9);
        std::queue<int> que;

        if (ptr == 0) {
            // 最初の変数はlit codeの出現頻度で決める
            int max_elm = *std::max_element(code_length_symbol_map[len].begin(), code_length_symbol_map[len].end(), [&](int a, int b) {
                return char_stats[a].num_nonvar_occurrences_as_literal < char_stats[b].num_nonvar_occurrences_as_literal;
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
        if (ptr >= replace_cand_vars.size()) break;
    }

    /*
    std::cout << "OLD STRING---------\n";
    for (auto c : text) {
        std::cout << static_cast<char>(c);
    }
    std::cout << "\n\n";
    */
   ptr = 0;
   for(auto i : replace_cand_vars) {
        if (variables[i].name.size() != 1) continue;
        int char_val = static_cast<int>(variables[i].name[0]);
        int new_val = assigned_literal_code[ptr++];
        if (new_val == -1) {
            continue;
        }
        std::cerr << "Rename: " << variables[i].name << " (" << char_val << ") -> '" << static_cast<char>(new_val) << "' (" << new_val << ")\n";
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
    block.tokens = optimal_parse_block(block, context);
}
