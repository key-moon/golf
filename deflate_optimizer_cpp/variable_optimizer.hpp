#pragma once
#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"
#include "variable.hpp"

void optimize_variables(DynamicHuffmanBlock& block, const std::vector<Variable>& variables, const std::vector<int>& context) {

    auto text = block.get_string(context);

    std::vector<bool> is_lieral_position(text.size());

    std::vector<int> literal_freq(256, 0);

    int ptr = 0;
    for(auto tok : block.tokens) {
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
    std::vector<std::pair<int,int>> considered_vars; // only single character variables, (char, lit_freq)

    for (int i = 0; i < variables.size(); ++i) {
        if (variables[i].name.size() != 1) continue;
        int char_val = static_cast<int>(variables[i].name[0]);
        considered_vars.emplace_back(char_val, num_lit_occurrences_of_vars[i]);
        literal_freq[char_val] -= num_lit_occurrences_of_vars[i]; // literal_freq only consider non-variable occurrences
    }
    std::sort(considered_vars.begin(), considered_vars.end(), [](const auto& a, const auto& b) {
        return a.second > b.second;
    });
    std::cout << "Considered variables: ";
    for (const auto& p : considered_vars) {
        std::cout << "'" << static_cast<char>(p.first) << "'(" << p.second << ") ";
    }
    std::cout << "\n";
    std::cout << "Literal frequencies after removing variable occurrences: ";
    for (int i = 0; i < literal_freq.size(); ++i) {
        if (literal_freq[i] > 0) {
            std::cout << "'" << static_cast<char>(i) << "'(" << literal_freq[i] << ")\n";
        }
    }
    std::vector<int> varid_variable_chars;
    for (int i = 'a'; i <= 'z'; ++i) varid_variable_chars.push_back(i);
    for (int i = 'A'; i <= 'Z'; ++i) varid_variable_chars.push_back(i);
    varid_variable_chars.push_back('_');
}
