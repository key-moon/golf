#pragma once
#include <cmath>
#include <numeric>

#include "blocks.hpp"
#include <algorithm>


void optimize_huffman_tree_by_DP(DynamicHuffmanBlock& block, const std::vector<int>& RLE_symbols_cost, int MAX_BIT_WIDTH=11) {
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

    int table_size = 0;
    std::vector<std::vector<std::vector<std::vector<int>>>> dp(lit_freq.size() + 1, std::vector<std::vector<std::vector<int>>>((1 << MAX_BIT_WIDTH) + 1, std::vector<std::vector<int>>(MAX_BIT_WIDTH + 1)));
    std::vector<std::vector<std::vector<std::vector<int>>>> prev_lens(lit_freq.size() + 1, std::vector<std::vector<std::vector<int>>>((1 << MAX_BIT_WIDTH) + 1, std::vector<std::vector<int>>(MAX_BIT_WIDTH + 1)));
    std::vector<std::vector<std::vector<std::vector<int>>>> prev_runs(lit_freq.size() + 1, std::vector<std::vector<std::vector<int>>>((1 << MAX_BIT_WIDTH) + 1, std::vector<std::vector<int>>(MAX_BIT_WIDTH + 1)));
    for (int i = 0; i <= lit_freq.size(); ++i) {
        for (int j = 0; j <= (1 << MAX_BIT_WIDTH); ++j) {
            for (int k = 0; k < MAX_BIT_WIDTH + 1; ++k) {
                dp[i][j][k].resize(k == 0 ? 138 : 10, 1e6);
                prev_lens[i][j][k].resize(k == 0 ? 138 : 10, -1);
                prev_runs[i][j][k].resize(k == 0 ? 138 : 10, -1);
                table_size += dp[i][j][k].size();
            }
        }
    }

    auto compute_run_cost = [&RLE_symbols_cost](int len, int run){
        int cost = RLE_symbols_cost[len] * run;
        if (4 <= run && run <= 7) {
            cost = std::min(cost, RLE_symbols_cost[len] + RLE_symbols_cost[16] + 2);
        }
        if (len == 0) {
            if (3 <= run && run <= 10) {
                cost = std::min(cost, RLE_symbols_cost[17] + 3);
            }
            if (11 <= run && run <= 138) {
                cost = std::min(cost, RLE_symbols_cost[18] + 7);
            }
        }
        return cost;
    };

    
    std::cout << "literal freqs: ";
    for (int i = 0; i < lit_freq.size(); ++i) {
        std::cout << lit_freq[i] << (i + 1 == lit_freq.size()
                ? "\n"
                : " ");
    }

    for (int len = 0; len <= MAX_BIT_WIDTH; ++len) {
        if (lit_freq[0] != 0 && len == 0) continue;
        int j = (1 << (MAX_BIT_WIDTH - len));
        dp[1][j][len][1] = lit_freq[0] * len;
    }
    for (int i = 1; i < lit_freq.size(); ++i) {
        for (int j = 0; j <= (1 << MAX_BIT_WIDTH); ++j) {
            for (int prev_len = 0; prev_len < MAX_BIT_WIDTH + 1; ++prev_len) {
                for (int prev_run = 0; prev_run < dp[i][j][prev_len].size(); ++prev_run) {
                    if (dp[i][j][prev_len][prev_run] == 1e6) continue;
                    for (int next_len = 0; next_len < MAX_BIT_WIDTH + 1; ++next_len) {
                        if (lit_freq[i] != 0 && next_len == 0) continue;
                        // Set as new run length
                        int next_j = j + (next_len == 0 ? 0 : (1 << (MAX_BIT_WIDTH - next_len)));
                        if (next_j > (1 << MAX_BIT_WIDTH)) continue;
                        int cost = dp[i][j][prev_len][prev_run] + compute_run_cost(prev_len, prev_run) + lit_freq[i] * next_len;
                        if (dp[i + 1][next_j][next_len][1] > cost) {
                            prev_lens[i + 1][next_j][next_len][1] = prev_len;
                            prev_runs[i + 1][next_j][next_len][1] = prev_run;
                            dp[i + 1][next_j][next_len][1] = cost;
                        }
                    }
                    // Extend the previous run
                    if (prev_run + 1 < dp[i][j][prev_len].size()) {
                        if (lit_freq[i] != 0 && prev_len == 0) continue;
                        if (prev_run + 1 >= dp[i + 1][j][prev_len].size()) continue;
                        int next_j = j + (prev_len == 0 ? 0 : (1 << (MAX_BIT_WIDTH - prev_len)));
                        if (next_j > (1 << MAX_BIT_WIDTH)) continue;
                        int cost = dp[i][j][prev_len][prev_run] + lit_freq[i] * prev_len;
                        if (dp[i + 1][next_j][prev_len][prev_run + 1] > cost) {
                            prev_lens[i + 1][next_j][prev_len][prev_run + 1] = prev_len;
                            prev_runs[i + 1][next_j][prev_len][prev_run + 1] = prev_run;
                            dp[i + 1][next_j][prev_len][prev_run + 1] = cost;
                        }
                    }
                }
            }
        }
    }
    const auto& dp_back = dp[lit_freq.size()][1 << MAX_BIT_WIDTH];
    std::tuple<int,int,int> best = {1e6, 1e6, 1e6};

    for (int prev_len = 0; prev_len < MAX_BIT_WIDTH + 1; ++prev_len) {
        for (int prev_run = 0; prev_run < dp_back[prev_len].size(); ++prev_run) {
            int cost = dp_back[prev_len][prev_run] + compute_run_cost(prev_len, prev_run);
            auto tup = std::make_tuple(cost, prev_len, prev_run);
            if (tup < best) {
                best = tup;
            }
        }
    }
    int best_cost = std::get<0>(best);
    int prev_len = std::get<1>(best);
    int prev_run = std::get<2>(best);

    int i = lit_freq.size();
    int j = 1 << MAX_BIT_WIDTH;
    std::vector<int> new_lit_code_lengths(lit_freq.size(), 0);
    while(i > 0) {
        new_lit_code_lengths[i - 1] = prev_len;
        int next_prev_len = prev_lens[i][j][prev_len][prev_run];
        int next_prev_run = prev_runs[i][j][prev_len][prev_run];
        if(prev_len) {
            j -= (1 << (MAX_BIT_WIDTH - prev_len));
        }
        prev_len = next_prev_len;
        prev_run = next_prev_run;
        i--;
    }
    block.literal_code_lengths = new_lit_code_lengths;
 }


void optimize_huffman_tree(DynamicHuffmanBlock& block) {

    constexpr int MAX_BIT_WIDTH = 11;

    std::vector<int> RLE_symbols_cost = {
        4, 0, 0, 4, 4,      // 0-4
        3, 3, 3, 5, 5,      // 5-9
        0, 0, 0, 0, 0, 0, // 10-15
        2, 4, 4
    };
    /*
    std::vector<int> RLE_symbols_cost = {
        0, 0, 0, 4, 4,      // 0-4
        2, 0, 2, 0, 0,      // 5-9
        0, 0, 0, 0, 0, 0, // 10-15
        2, 4, 4
    };
    */
    while(RLE_symbols_cost.size() && RLE_symbols_cost.back() == 0) RLE_symbols_cost.pop_back();
    for (int i = 0; i < RLE_symbols_cost.size(); ++i) {
        if (RLE_symbols_cost[i] == 0) RLE_symbols_cost[i] = 1e6;
    }

    for (int iter = 0; iter < 10; ++iter) {
        std::cout << "Iteration " << iter << std::endl;
        std::cout << "Before optimization: " << block.bit_length() << std::endl;
        std::cout << "Literal code lengths: ";
        int before_bit_length = block.bit_length();
        auto before_literal_code_lengths = block.literal_code_lengths;
        for (int i = 0; i < block.literal_code_lengths.size(); ++i) {
            int length = block.literal_code_lengths[i] == 1e6 ? -1 : block.literal_code_lengths[i];
            std::cout << length << (i + 1 == block.literal_code_lengths.size() ? "\n" : " ");
        }
        std::cout << "RLE code lengths: ";
        for (int i = 0; i < RLE_symbols_cost.size(); ++i) {
            int length = RLE_symbols_cost[i] == 1e6 ? -1 : RLE_symbols_cost[i];
            std::cout << length << (i + 1 == RLE_symbols_cost.size() ? "\n" : " ");
        }

        optimize_huffman_tree_by_DP(block, RLE_symbols_cost);

        auto cl_code_lengths = block.get_cl_code_lengths();
        RLE_symbols_cost = cl_code_lengths;
        while(RLE_symbols_cost.size() && RLE_symbols_cost.back() == 0) RLE_symbols_cost.pop_back();
        for (int i = 0; i < RLE_symbols_cost.size(); ++i) {
            if (RLE_symbols_cost[i] == 0) RLE_symbols_cost[i] = 1e6;
        }

        std::cout << "After optimization: " << block.bit_length() << std::endl;
        std::cout << std::endl;

        if (before_bit_length <= block.bit_length()) {
            block.literal_code_lengths = before_literal_code_lengths;
            std::cout << "No improvement, stop optimization." << std::endl;
            break;
        }
    }
    std::cout << "Final bit length: " << block.bit_length() << std::endl;
}
