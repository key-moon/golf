#pragma once
#include <algorithm>
#include <cmath>
#include <numeric>

#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimal_lit_code_lengths.hpp"
#include "xorshift.hpp"


void randomly_update_code_lengths(std::vector<int>& code_lengths, int MAX_BIT_WIDTH=7) {
    /*
    符号長総和を維持するような近傍操作:
    - 符号長swap（隣接する確率を高く）
    - 1要素を1短くし、同じ長さの2要素を1長くする (333->244)
    */
    std::vector<std::vector<int>> length_buckets(MAX_BIT_WIDTH + 1);
    for (int i = 0; i < code_lengths.size(); ++i) {
        length_buckets[code_lengths[i]].push_back(i);
    }
    int idx = 0;
    while (true) {
        int move = XorShift::randn(5);
        if (move == 0) {
            int target1, target2;
            target1 = XorShift::randn(code_lengths.size());
            if (code_lengths[target1] == 0) continue;
            std::vector<int> candidates;
            if (code_lengths[target1] > 1) {
                candidates.insert(candidates.end(), length_buckets[code_lengths[target1] - 1].begin(), length_buckets[code_lengths[target1] - 1].end());
            }
            if (code_lengths[target1] < MAX_BIT_WIDTH) {
                candidates.insert(candidates.end(), length_buckets[code_lengths[target1] + 1].begin(), length_buckets[code_lengths[target1] + 1].end());
            }
            if (candidates.size() == 0) continue;
            target2 = candidates[XorShift::randn(candidates.size())];
            std::swap(code_lengths[target1], code_lengths[target2]);
            // std::cerr << "Operated: adjacent swap " << target1 << " " << target2 << std::endl;
            break;
        } else if (move == 1) {
            // random swap
            int target1 = XorShift::randn(code_lengths.size());
            int target2 = XorShift::randn(code_lengths.size());
            if (target1 == target2) continue;
            if (code_lengths[target1] == code_lengths[target2]) continue;
            if (code_lengths[target1] == 0 || code_lengths[target2] == 0) continue;
            std::swap(code_lengths[target1], code_lengths[target2]);
            // std::cerr << "Operated: random swap " << target1 << " " << target2 << std::endl;
            break;
        } else {
            if (move == 2) {
                std::vector<int> candidate_lengths;
                for (int len = 1; len <= MAX_BIT_WIDTH; ++len) {
                    if (length_buckets[len].size() >= 2) {
                        candidate_lengths.push_back(len);
                    }
                }
                if (candidate_lengths.empty()) continue;
                int target_len = candidate_lengths[XorShift::randn(candidate_lengths.size())];
                auto perm = XorShift::rand_perm(length_buckets[target_len].size());
                int to_zero = length_buckets[target_len][perm[0]];
                int to_shorten = length_buckets[target_len][perm[1]];
                code_lengths[to_zero] = 0;
                --code_lengths[to_shorten];
                // std::cerr << "Operated: zero + shorten " << to_zero << " " << to_shorten << std::endl;
                break;
            } else if (move == 3) {
                if (length_buckets[0].empty()) continue;
                std::vector<int> non_zero_candidates;
                for (int len = 1; len < MAX_BIT_WIDTH; ++len) {
                    non_zero_candidates.insert(non_zero_candidates.end(), length_buckets[len].begin(), length_buckets[len].end());
                }
                if (non_zero_candidates.empty()) continue;
                int zero_idx = length_buckets[0][XorShift::randn(length_buckets[0].size())];
                int target_idx = non_zero_candidates[XorShift::randn(non_zero_candidates.size())];
                int new_length = code_lengths[target_idx] + 1;
                if (new_length > MAX_BIT_WIDTH) continue;
                ++code_lengths[target_idx];
                code_lengths[zero_idx] = new_length;
                // std::cerr << "Operated: zero to match extended " << zero_idx << " " << target_idx << std::endl;
                break;
            } else {
                int target_len = XorShift::randn(MAX_BIT_WIDTH - 1) + 1;
                if (length_buckets[target_len].size() < 3) continue;
                auto perm = XorShift::rand_perm(length_buckets[target_len].size());
                --code_lengths[length_buckets[target_len][perm[0]]];
                ++code_lengths[length_buckets[target_len][perm[1]]];
                ++code_lengths[length_buckets[target_len][perm[2]]];
                // std::cerr << "Operated: length change (++-) " << length_buckets[target_len][perm[0]] << " " << length_buckets[target_len][perm[1]] << " " << length_buckets[target_len][perm[2]] << std::endl;
                break;
            }
        }
    }
}

void optimize_huffman_tree(DynamicHuffmanBlock& block, const std::vector<int>& context, bool perturbation, int num_iter = 10) {

    // std::cerr << "Initial Block bit length: " << block.bit_length() << std::endl;
    auto best = std::make_pair(block.bit_length(), block.cl_code_lengths);

    auto get_optimal_parse_iteration = [&block, &context](int max_iter=10) {
        auto best = std::make_tuple(block.bit_length(), block.cl_code_lengths, block.tokens);
        std::vector<std::vector<int>> tried_cl_code_lengths;
        tried_cl_code_lengths.push_back(block.cl_code_lengths);
        for (int iter = 0; iter < max_iter; ++iter) {
            // parsingを求めてから符号長を更新
            block.tokens = optimal_parse_block(block, context);
            block.cl_code_lengths = block.get_optimal_cl_code_lengths();
            int bit_length = block.bit_length();
            if (bit_length <= std::get<0>(best)) {
                best = std::make_tuple(bit_length, block.cl_code_lengths, block.tokens);
            }
            if (std::find(tried_cl_code_lengths.begin(), tried_cl_code_lengths.end(), block.cl_code_lengths) != tried_cl_code_lengths.end()) {
                // 既に試した符号長に戻ったら終了
                break;
            }
            tried_cl_code_lengths.push_back(block.cl_code_lengths);
        }
        block.cl_code_lengths = std::get<1>(best);
        block.tokens = std::get<2>(best);
    };

    bool updated = true;

    for (int iter = 0; iter < num_iter; ++iter) {
        // std::cerr << "----------------------------------------" << std::endl;
        // std::cerr << "Iteration " << iter << std::endl;
        if (!updated) {
            randomly_update_code_lengths(block.cl_code_lengths, 7);
            /*
            std::cerr << "CL_lengths:  ";
            for (int i = 0; i < block.cl_code_lengths.size(); ++i) {
                std::cerr << (block.cl_code_lengths[i] == 1e6 ? 0 : block.cl_code_lengths[i]) << (i + 1 == block.cl_code_lengths.size() ? "\n" : " ");
            }
            */
        }
        else {
            /*
            std::cerr << "CL_lengths:  ";
            for (int i = 0; i < block.cl_code_lengths.size(); ++i) {
                std::cerr << (block.cl_code_lengths[i] == 1e6 ? 0 : block.cl_code_lengths[i]) << (i + 1 == block.cl_code_lengths.size() ? "\n" : " ");
            }
            */
        }
        optimize_lit_code_huffman(block);
        optimize_dist_code_huffman(block);

        auto old_cl_code_lengths = block.cl_code_lengths;
        auto old_tokens = block.tokens;
        get_optimal_parse_iteration();

        if (old_cl_code_lengths != block.cl_code_lengths || old_tokens != block.tokens) {
            updated = true;
        } else {
            updated = false;
        }
        int bit_length = block.bit_length();
        if (bit_length <= best.first) {
            best = std::make_pair(bit_length, block.cl_code_lengths);
        } else if (!updated) {
            block.cl_code_lengths = best.second;
            if (!perturbation) {
                break;
            }
        }
        // std::cerr << "Block bit length: " << block.bit_length() << std::endl;
        // std::cerr << "----------------------------------------" << std::endl;
        // std::cerr << std::endl;
    }
    optimize_lit_code_huffman(block);
    optimize_dist_code_huffman(block);
}
