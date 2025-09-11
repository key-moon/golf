#pragma once
#include <algorithm>
#include <cmath>
#include <numeric>

#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimal_lit_code_lengths.hpp"


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

void optimize_huffman_tree(DynamicHuffmanBlock& block, int num_iter = 100) {

    std::cout << "Initial Block bit length: " << block.bit_length() << std::endl;
    auto best = std::make_pair(block.bit_length(), block.cl_code_lengths);


    auto get_optimal_parse_iteration = [&block](int max_iter=10) {
        auto best = std::make_tuple(block.bit_length(), block.cl_code_lengths, block.tokens);
        for (int iter = 0; iter < max_iter; ++iter) {
            // parsingを求めてから符号長を更新
            block.tokens = optimal_parse_block(block, std::vector<int>());
            block.cl_code_lengths = block.get_optimal_cl_code_lengths();
            int bit_length = block.bit_length();
            if (bit_length <= std::get<0>(best)) {
                best = std::make_tuple(bit_length, block.cl_code_lengths, block.tokens);
            } else if (block.cl_code_lengths == std::get<1>(best) && block.tokens == std::get<2>(best)) {
                // 変化がなければ終了
                break;
            }
        }
        block.cl_code_lengths = std::get<1>(best);
        block.tokens = std::get<2>(best);
    };

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
        optimize_lit_code_huffman(block);

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
        } else {
            if (!updated) {
                block.cl_code_lengths = best.second;
            }
        }
        std::cout << "Block bit length: " << block.bit_length() << std::endl;
        std::cout << "----------------------------------------" << std::endl;
        std::cout << std::endl;
    }
    optimize_lit_code_huffman(block);
}
