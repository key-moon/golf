#pragma once
#include <algorithm>

#include "blocks.hpp"

std::vector<Token> optimal_parse_block(CompressedBlock& block, const std::vector<int>& context) {

    std::vector<int> block_text = block.get_string(context);
    std::vector<int> overall_text = context;
    overall_text.insert(overall_text.end(), block_text.begin(), block_text.end());
    int n = block_text.size();
    int m = overall_text.size();
    std::vector<std::vector<int>> lcp(n + 1, std::vector<int>(m + 1, 0));
    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            if (block_text[i] == overall_text[j]) {
                lcp[i][j] = lcp[i + 1][j + 1] + 1;
            } else {
                lcp[i][j] = 0;
            }
        }
    }
    // g[i][j]: (bit_length, distance) for block_text[i..j)
    std::vector<std::vector<std::pair<int,int>>> g(n + 1, std::vector<std::pair<int,int>>(n + 1, {1e9, 1e9}));
    std::vector<int> max_match(n, 1);
    for (int i = 0; i < n; ++i) {
        g[i][i + 1] = {block.get_literal_code_length(block_text[i]), -1};
    }
    for (int i = 0; i < n; ++i) {
        for (int ref = 0; ref < context.size() + i; ++ref) {
            int lcp_len = lcp[i][ref];
            lcp_len = std::min(lcp_len, 258); // deflateの最大長
            max_match[i] = std::max(max_match[i], lcp_len);
            int dist = (i + context.size()) - ref;
            int dist_cost = block.get_distance_code_length(convert_distance_value_to_code(dist)) + num_additional_bits_for_dist(dist);
            if (dist_cost >= 1e9) continue;
            for (int len = 3; len <= lcp_len; ++len) {
                int len_cost = block.get_literal_code_length(convert_length_value_to_code(len)) + num_additional_bits_for_len(len);
                if (len_cost >= 1e9) continue;
                int cost = len_cost + dist_cost;
                g[i][i + len] = std::min(g[i][i + len], {cost, dist});
            }
        }
    }
    std::vector<int> dp(n + 1, 1e9);
    std::vector<int> prev(n + 1, 1e9);
    dp[0] = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j <= i + max_match[i]; ++j) {
            auto [cost, dist] = g[i][j];
            if (dp[i] + cost <= dp[j]) {
                dp[j] = dp[i] + cost;
                prev[j] = i;
            }
        }
    }
    if (dp[n] == 1e9) {
        throw std::runtime_error("Could not find any path in matching graph");
    }
    std::vector<Token> tokens;
    int now = n;
    while(now) {
        int p = prev[now];
        int len = now - p;
        int dist = g[p][now].second;
        if (len != 1) {
            if (dist == 1e9) {
                throw std::runtime_error("Invalid distance");
            }
            tokens.push_back(Token{ Token::COPY, .pair = { len, dist }});
        }
        else {
            tokens.push_back(Token{ Token::LITERAL, .literal = static_cast<unsigned char>(block_text[p])});
        }
        now = p;
    }
    std::reverse(tokens.begin(), tokens.end());
    return tokens;
}

void optimal_parse(std::vector<std::unique_ptr<Block>>& blocks){
    std::vector<int> text;
    for(auto& block: blocks){
        if(auto* cblock = dynamic_cast<CompressedBlock*>(block.get())){
            auto blk_text = block->get_string(text);
            auto tokens = optimal_parse_block(*cblock, text);
            text.insert(text.end(), blk_text.begin(), blk_text.end());
            cblock->tokens = tokens;
        }
    }
}


std::vector<Token> longest_greedy_parse_block(CompressedBlock& block, const std::vector<int>& context) {
    // O(n^2) implementation
    std::vector<int> block_text = block.get_string(context);
    std::vector<int> overall_text = context;
    overall_text.insert(overall_text.end(), block_text.begin(), block_text.end());
    int n = block_text.size();
    int m = overall_text.size();
    std::vector<std::vector<int>> lcp(n + 1, std::vector<int>(m + 1, 0));
    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            if (block_text[i] == overall_text[j]) {
                lcp[i][j] = lcp[i + 1][j + 1] + 1;
            } else {
                lcp[i][j] = 0;
            }
        }
    }
    // g[i]: (bit_length, distance) for block_text[i..(i+max_match[i]))
    std::vector<std::pair<int,int>> g(n + 1, {1e9, 1e9});
    int i = 0;
    std::vector<Token> tokens;
    int sum_cost = 0;
    while(i != n) {
        // max_match, -min_cost, distance
        std::tuple<int,int,int> state = { 1, -block.get_literal_code_length(block_text[i]), -1 };
        for (int ref = 0; ref < context.size() + i; ++ref) {
            int lcp_len = lcp[i][ref];
            for (int len = lcp_len; len >= 3; --len) {

                int len_cost = block.get_literal_code_length(convert_length_value_to_code(len)) + num_additional_bits_for_len(len);
                int dist = (i + context.size()) - ref;
                int dist_cost = block.get_distance_code_length(convert_distance_value_to_code(dist)) + num_additional_bits_for_dist(dist);
                if (len_cost >= 1e9 || dist_cost >= 1e9) continue;
                int cost = len_cost + dist_cost;
                std::tuple<int,int,int> tup = { lcp_len, -cost, dist};
                state = std::max(state, tup);
                break;
            }
        }
        auto [len, cost, dist] = state;
        sum_cost -= cost;
        if (len != 1) {
            if (dist == 1e9) {
                throw std::runtime_error("Invalid distance");
            }
            tokens.push_back(Token{ Token::COPY, .pair = { len, dist }});
        }
        else {
            tokens.push_back(Token{ Token::LITERAL, .literal = static_cast<unsigned char>(block_text[i])});
        }
        i += len;
    }
    return tokens;
}

void longest_greedy_parse(std::vector<std::unique_ptr<Block>>& blocks){
    std::vector<int> text;
    for(auto& block: blocks){
        if(auto* cblock = dynamic_cast<CompressedBlock*>(block.get())){
            auto blk_text = block->get_string(text);
            auto tokens = longest_greedy_parse_block(*cblock, text);
            text.insert(text.end(), blk_text.begin(), blk_text.end());
            cblock->tokens = tokens;
        }
    }
}
