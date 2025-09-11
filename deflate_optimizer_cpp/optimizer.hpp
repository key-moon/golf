#pragma once
#include <cmath>
#include <numeric>

#include "blocks.hpp"
#include <algorithm>


namespace XorShift{
  uint64_t rnd_val = 0xdeadbeefcafebabe;
  uint64_t rand(){ rnd_val ^= rnd_val << 7; rnd_val ^= rnd_val >> 9; return rnd_val; }
  double rand_double(){ return double(rand()) / UINT64_MAX; }
  template<int N>
  int randn(){ return (uint64_t(uint32_t(rand())) * N) >> 32; }
  int randn(int n){ return (uint64_t(uint32_t(rand())) * n) >> 32; }
  std::vector<int> rand_perm(int n){
    std::vector<int> v(n);
    std::iota(v.begin(), v.end(), 0);
    for(int i = n - 1; i >= 1; --i){
      int j = randn(i + 1);
      std::swap(v[i], v[j]);
    }
    return v;
  }
  template<typename T>
  void shuffle(std::vector<T>& v){
    int n = v.size();
    for(int i = n - 1; i >= 1; --i){
      int j = randn(i + 1);
      std::swap(v[i], v[j]);
    }
  }
};


void optimize_huffman_tree_by_DP(DynamicHuffmanBlock& block, int MAX_BIT_WIDTH=11) {
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
        double prob = XorShift::rand_double();
        if (prob < 0.5) {
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
            std::cout << "Operated: adjacent swap " << target1 << " " << target2 << std::endl;
            break;
        } else if (prob < 0.75) {
            // random swap
            int target1 = XorShift::randn(code_lengths.size());
            int target2 = XorShift::randn(code_lengths.size());
            if (target1 == target2) continue;
            if (code_lengths[target1] == code_lengths[target2]) continue;
            if (code_lengths[target1] == 0 || code_lengths[target2] == 0) continue;
            std::swap(code_lengths[target1], code_lengths[target2]);
            std::cout << "Operated: random swap " << target1 << " " << target2 << std::endl;
            break;
        } else {
            int target_len = XorShift::randn(MAX_BIT_WIDTH - 1) + 1;
            if (length_buckets[target_len].size() < 3) continue;
            auto perm = XorShift::rand_perm(length_buckets[target_len].size());
            --code_lengths[length_buckets[target_len][perm[0]]];
            ++code_lengths[length_buckets[target_len][perm[1]]];
            ++code_lengths[length_buckets[target_len][perm[2]]];
            std::cout << "Operated: length change (++-) " << length_buckets[target_len][perm[0]] << " " << length_buckets[target_len][perm[1]] << " " << length_buckets[target_len][perm[2]] << std::endl;
            break;
        }
    }
}

void optimize_huffman_tree(DynamicHuffmanBlock& block, int num_iter = 5) {
    std::cout << "Initial Block bit length: " << block.bit_length() << std::endl;
    auto best = std::make_pair(block.bit_length(), block.cl_code_lengths);

    bool updated = true;

    for (int iter = 0; iter < num_iter; ++iter) {
        std::cout << "----------------------------------------" << std::endl;
        std::cout << "Iteration " << iter << std::endl;
        if (!updated) {
            randomly_update_code_lengths(block.cl_code_lengths, 7);
            std::cout << "CL_lengths:  ";
            for (int i = 0; i < block.cl_code_lengths.size(); ++i) {
                std::cout << (block.cl_code_lengths[i] == 1e6 ? 0 : block.cl_code_lengths[i]) << (i + 1 == block.cl_code_lengths.size() ? "\n" : " ");
            }
        }
        else {
            std::cout << "CL_lengths:  ";
            for (int i = 0; i < block.cl_code_lengths.size(); ++i) {
                std::cout << (block.cl_code_lengths[i] == 1e6 ? 0 : block.cl_code_lengths[i]) << (i + 1 == block.cl_code_lengths.size() ? "\n" : " ");
            }
        }
        optimize_huffman_tree_by_DP(block);
        auto cl_code_lengths = block.get_optimal_cl_code_lengths();
        if (cl_code_lengths != block.cl_code_lengths) {
            block.cl_code_lengths = cl_code_lengths;
            updated = true;
        } else {
            updated = false;
        }
        int bit_length = block.bit_length();
        if (bit_length <= best.first) {
            best = std::make_pair(bit_length, block.cl_code_lengths);
        } else {
            if (!updated) {
                block.cl_code_lengths = best.second;
            }
        }
        std::cout << "Block bit length: " << block.bit_length() << std::endl;
        std::cout << "----------------------------------------" << std::endl;
        std::cout << std::endl;
    }
    optimize_huffman_tree_by_DP(block);
}
