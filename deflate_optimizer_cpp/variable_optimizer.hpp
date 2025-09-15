#pragma once
#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"
#include "variable.hpp"



// only single char variables are supported for now
void rename_variables(std::vector<Token>& tokens, const std::vector<Variable>& variables, const std::vector<int>& var_char_mapping) {
    std::vector<int> text_position_to_variable_id;
    for (int var_id = 0; var_id < variables.size(); ++var_id) {
        for (auto pos : variables[var_id].occurrences) {
            if (text_position_to_variable_id.size() <= pos) {
                text_position_to_variable_id.resize(pos + 1, -1);
            }
            text_position_to_variable_id[pos] = var_id;
        }
    }
    int ptr = 0;
    for (int i = 0; i < tokens.size(); ++i) {
        if (tokens[i].type == Token::LITERAL) {
            if (text_position_to_variable_id[ptr] != -1) {
                if (variables[text_position_to_variable_id[ptr]].name.size() != 1) continue;
                int var_char = static_cast<int>(variables[text_position_to_variable_id[ptr]].name[0]);
                if (var_char_mapping[var_char] == -1) continue;
                tokens[i].literal = static_cast<unsigned char>(var_char_mapping[var_char]);
                // std::cout << "Renamed literal at position " << ptr << " (char=" << static_cast<char>(var_char) << ") to variable char '" << static_cast<char>(tokens[i].literal) << "' (" << (int)tokens[i].literal << ")\n";
            }
            ptr += 1;
        }
        else {
            ptr += tokens[i].pair.length;
        }
    }
}


void optimize_variables(DynamicHuffmanBlock& block, const std::vector<Variable>& variables, const std::vector<int>& context) {

    auto text = block.get_string(context);

    /*
    std::cout << "-------- Code --------\n";
    for (auto c : text) {
        std::cout << static_cast<char>(c);
    }
    std::cout << "\n\n";
    */



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

    std::vector<int> num_lit_occurrences_of_vars(variables.size(), 0);
    for (int i = 0; i < variables.size(); ++i) {
        for (auto pos : variables[i].occurrences) {
            for (int j = 0; j < variables[i].name.size(); ++j) {
                if (text[pos + j] != static_cast<int>(variables[i].name[j])) {
                    std::cerr << "Error: variable occurrence does not match variable name\n";
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
    for (int i = 'a'; i <= 'z'; ++i) char_stats[i].var_candidate = true;
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

    /*
    std::cout << "-------- Variable Candidates (var_occ, nonvar_occ, lit_code_length) --------\n";
    for (int i = 0; i < 256; ++i) {
        if (!char_stats[i].var_candidate) continue;
        std::cout << "Char '" << static_cast<char>(i) << "' (" << i << "): ";
        std::cout << char_stats[i].num_var_occurrences_as_literal << ", ";
        std::cout << char_stats[i].num_nonvar_occurrences_as_literal << ", ";
        std::cout << char_stats[i].lit_code_length 
         << "\n";
    }
    */

    // とりあえず、ビット数が少ないところに貪欲に当てはめていく
    // ビット数が同じ場合、既に埋めたところに近いものを優先的に割り当てる感じで
    struct VarStat {
        int original_char;
        int num_var_occurrences_as_literal;
    };

    std::vector<VarStat> vars; // 変数をliteralとしての出現回数でソート
    for (int i = 0; i < 256; ++i) {
        if (!char_stats[i].var_candidate) continue;
        if (char_stats[i].num_var_occurrences_as_literal == 0) continue;
        // std::cout << "Variable candidate: '" << static_cast<char>(i) << "' (" << i << ") with " << char_stats[i].num_var_occurrences_as_literal << " literal occurrences\n";
        vars.push_back({i, char_stats[i].num_var_occurrences_as_literal});
    }
    std::sort(vars.begin(), vars.end(), [](const VarStat& a, const VarStat& b) {
        if (a.num_var_occurrences_as_literal != b.num_var_occurrences_as_literal) {
            return a.num_var_occurrences_as_literal > b.num_var_occurrences_as_literal;
        }
        return a.original_char < b.original_char;
    });

    std::vector<int> assigned_literal_code(256, -1); // 変数文字 -> 割り当てたliteralコード

    std::vector<std::vector<int>> code_length_symbol_map(17);
    for (int i = 0; i < 256; ++i) {
        if (!char_stats[i].var_candidate) continue;
        code_length_symbol_map[char_stats[i].lit_code_length].push_back(i);
    }
    ptr = 0;
    for (int len = 1; len <= 16; ++len) {
        // std::cout << "Length " << len << ": " << code_length_symbol_map[len].size() << " candidates\n";
        if (code_length_symbol_map[len].size() == 0) continue;
        std::vector<int> traverse_vars_list;
        std::vector<int> distance_vec(256, 1e9);
        std::queue<int> que;


        if (ptr == 0) {
            // 最初の変数はlit codeの出現頻度で決める
            std::sort(code_length_symbol_map[len].begin(), code_length_symbol_map[len].end(), [&](int a, int b) {
                return char_stats[a].num_nonvar_occurrences_as_literal > char_stats[b].num_nonvar_occurrences_as_literal;
            });
            assigned_literal_code[vars[ptr].original_char] = code_length_symbol_map[len][0];
            ++ptr;
        }

        for (int j = 0; j < 256; ++j) {
            if (assigned_literal_code[j] != -1) {
                distance_vec[j] = 0;
                que.push(j);
            }
        }
        while (!que.empty()) {
            int v = que.front();
            que.pop();
            if (char_stats[v].lit_code_length == len) {
                traverse_vars_list.push_back(v);
            }
            for (int u : code_length_symbol_map[len]) {
                if (distance_vec[u] > distance_vec[v] + 1) {
                    distance_vec[u] = distance_vec[v] + 1;
                    que.push(u);
                }
            }
        }
        // std::cout << "traverse_vars_list size: " << traverse_vars_list.size() << "\n";
        for(auto var : traverse_vars_list) {
            assigned_literal_code[vars[ptr].original_char] = var;
            ++ptr;
            if (ptr >= vars.size()) break;
        }
        if (ptr >= vars.size()) break;
    }

    /*
    std::cout << "OLD STRING---------\n";
    for (auto c : text) {
        std::cout << static_cast<char>(c);
    }
    std::cout << "\n\n";
    */
    rename_variables(block.tokens, variables, assigned_literal_code);
    /*
    std::cout << "NEW STRING---------\n";
    text = block.get_string(context);
    for (auto c : text) {
        std::cout << static_cast<char>(c);
    }
    std::cout << "\n\n";
    */
}
