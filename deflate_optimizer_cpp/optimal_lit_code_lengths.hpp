#pragma once
#include "blocks.hpp"

void optimize_lit_code_huffman(DynamicHuffmanBlock& block, int MAX_BIT_WIDTH=9) {
    std::vector<int> lit_freq(286, 0);
    std::vector<int> dist_freq(30, 0);
    for (const auto& token : block.tokens) {
        if (token.type == Token::LITERAL) {
            lit_freq[token.literal]++;
        } else {
            int len_code = convert_length_value_to_code(token.pair.length);
            int dist_code = convert_distance_value_to_code(token.pair.distance);
            lit_freq[len_code]++;
            dist_freq[dist_code]++;
        }
    }
    lit_freq[256] = 1;
    while(lit_freq.size() > 257 && lit_freq.back() == 0) lit_freq.pop_back();
    while(dist_freq.size() > 1 && dist_freq.back() == 0) dist_freq.pop_back();

    std::vector<std::vector<std::vector<int>>> dp(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, 1e6)));
    std::vector<std::vector<std::vector<int>>> last_run_code(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, -1)));
    std::vector<std::vector<std::vector<int>>> last_run_length(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, -1)));

    std::vector<int> RLE_symbols_cost = block.cl_code_lengths;
    for(auto& l : RLE_symbols_cost) {
        if (l == 0) l = 1e6;
    }

    auto compute_run_cost = [&RLE_symbols_cost](int prev_code, int last_run_code, int last_run_length) {
        if (last_run_length == 1) {
            return RLE_symbols_cost[last_run_code];
        }
        else if(prev_code == last_run_code) {
            if (3 <= last_run_length && last_run_length <= 6) {
                return RLE_symbols_cost[16] + 2;
            }
        } else if (last_run_code == 0) {
            if (3 <= last_run_length && last_run_length <= 10) {
                return RLE_symbols_cost[17] + 3;
            }
            else if (11 <= last_run_length && last_run_length <= 138) {
                return RLE_symbols_cost[18] + 7;
            }
        }
        return (int)1e6;
    };
    
    dp[0][0][MAX_BIT_WIDTH] = 0;

    for (int i = 0; i < lit_freq.size(); ++i) {
        for (int j = 0; j <= (1 << MAX_BIT_WIDTH); ++j) {
            for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
                if (dp[i][j][prev_code] == 1e6) continue;
                for (int code = 0; code <= MAX_BIT_WIDTH; ++code) {
                    int maximum_length = code == 0 ? 138 : 6;
                    int next_j = j;
                    int lit_cost = 0;
                    for (int run_length = 1; run_length <= maximum_length; ++run_length) {
                        if (i + run_length >= dp.size()) break;
                        next_j += (code == 0 ? 0 : (1 << (MAX_BIT_WIDTH - code)));
                        lit_cost += lit_freq[i + run_length - 1] * code;
                        if (lit_freq[i + run_length - 1] != 0 && code == 0) break;
                        if (next_j > (1 << MAX_BIT_WIDTH)) break;
                        int run_cost = compute_run_cost(prev_code, code, run_length);
                        int cost = dp[i][j][prev_code] + run_cost + lit_cost;
                        if (dp[i + run_length][next_j][code] > cost) {
                            dp[i + run_length][next_j][code] = cost;
                            last_run_code[i + run_length][next_j][code] = prev_code;
                            last_run_length[i + run_length][next_j][code] = run_length;
                        }
                    }
                }
            }
        }
    }

    const auto& dp_back = dp[lit_freq.size()][(1 << MAX_BIT_WIDTH)];
    std::pair<int,int> best = {1e6, 1e6};
    for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
        int cost = dp_back[prev_code];
        auto p = std::make_pair(cost, prev_code);
        if (p < best) {
            best = p;
        }
    }
    int best_cost = best.first;
    int code = best.second;
    std::vector<int> new_lit_code_lengths(lit_freq.size(), 0);
    int i = lit_freq.size();
    int j = (1 << MAX_BIT_WIDTH);
    while(i > 0) {
        int prev_code = last_run_code[i][j][code];
        int run_length = last_run_length[i][j][code];
        for (int k = 0; k < run_length; ++k) {
            new_lit_code_lengths[--i] = code;
            j -= (code == 0 ? 0 : (1 << (MAX_BIT_WIDTH - code)));
        }
        code = prev_code;
    }
    block.literal_code_lengths = new_lit_code_lengths;
 }
