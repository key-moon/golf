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


void optimize_huffman_tree(DynamicHuffmanBlock& block) {
    /*
    literal/length huffman treeを最適化する
    distance huffman treeはRLEが同じとはいえ完全に違う分布なので、こっちは変更を近傍に入れない
    特に、lit/lenとdistanceの間でRLEを共有しないような実装にする
    
    近傍:
    - litを1つ選んでlengthを縮める
      - この際に、Kraftの不等式を満たすようにずらす必要がある
      - 同じ長さを1つ伸ばすか、1つ長いものを2つ伸ばすか
    - 2点の長さをswap
    - 使っていないsymbolを1つ選んでlength=INFにする
    - 使っていないsymbolを1つ選んでlength=（割り当てられているうちのmax）にする

    Kreftの不等式違反はバリア関数でいい？

    TODO:
    - RLEの端を増減させるような実装ができると嬉しい
    */

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
    // TODO: これを使った差分更新をすると早くなるが、今の実装でも length<=300 ぐらいなので一旦これで
    // std::vector<RLEEntry> lit_RLE_entries = length_RLE(block.literal_code_lengths);
    // std::vector<RLEEntry> dist_RLE_entries = length_RLE(block.distance_code_lengths);

    while(lit_freq.size() > 257 && lit_freq.back() == 0) lit_freq.pop_back();
    while(dist_freq.size() > 1 && dist_freq.back() == 0) dist_freq.pop_back();


    // Starting from freq-huffman:
    // block.literal_code_lengths = compute_huff_code_lengths_from_frequencies(lit_freq);

    // Starting from fixed-huffman code lengths:
    // block.literal_code_lengths = std::vector<int>(286, 8);
    // for (int i = 0; i <= 143; ++i) if(i < block.literal_code_lengths.size()) block.literal_code_lengths[i] = 8;
    // for (int i = 144; i <= 255; ++i) if(i < block.literal_code_lengths.size()) block.literal_code_lengths[i] = 9;
    // for (int i = 256; i <= 279; ++i) if(i < block.literal_code_lengths.size()) block.literal_code_lengths[i] = 7;
    // for (int i = 280; i <= 285; ++i) if(i < block.literal_code_lengths.size()) block.literal_code_lengths[i] = 8;

    constexpr int MAX_BIT_WIDTH = 16;

    int kreft_value = 0;
    for (int len : block.literal_code_lengths) {
        if (len > 0) {
            kreft_value += (1 << (MAX_BIT_WIDTH - len));
        }
    }

    constexpr int MAX_ITER = 100000;
    constexpr double ALPHA = 1e9; // penalty for exceeding Kreft's bound
    constexpr double BETA = 0;  // reward for being below Kreft's bound

    auto RLE_part_code_length = [&](const std::vector<int>& lit_code_lengths, const std::vector<int>& dist_code_lengths) -> int {
        std::vector<RLECode> rle_codes = compute_RLE_encoded_representation(lit_code_lengths, dist_code_lengths);
        std::vector<int> cl_frequencies(19, 0);
        for (const auto& code : rle_codes) {
            cl_frequencies[code.id()]++;
        }
        std::vector<int> cl_code_lengths = compute_huff_code_lengths_from_frequencies(cl_frequencies);
        int hclen = 0;
        for (int i = 18; i >= 0; --i) {
            if (cl_code_lengths[CL_CODE_ORDER[i]] > 0) {
                hclen = i + 1;
                break;
            }
        }
        int length = hclen * 3;
        for (auto& code : rle_codes) {
            length += cl_code_lengths[code.id()];
            length += code.num_additional_bits();
        }
        return length;
    };
    auto kreft_penalty = [&](int kreft_value, double t) -> int {
        double time_pena = log(1.0 / (1.0 - t));
        double diff = static_cast<double>(kreft_value) / (1 << MAX_BIT_WIDTH) - 1.0;
        if (diff > 0.0) {
            return time_pena * diff * ALPHA;
        } else {
            return time_pena * diff * BETA;
        }
    };

    for (int iter = 0; iter < MAX_ITER; ++iter) {
        double t = static_cast<double>(iter) / MAX_ITER;
        int new_kreft_value = kreft_value;
        int body_length_diff = 0;
        auto old_lit_code_lengths = block.literal_code_lengths;
        int max_len = *std::max_element(block.literal_code_lengths.begin(), block.literal_code_lengths.end());

        int target = XorShift::randn(block.literal_code_lengths.size());
        int old_len = block.literal_code_lengths[target];

        if (old_len == 0) {
            // assert lit_freq[target] == 0
            block.literal_code_lengths[target] = max_len;
            new_kreft_value += (1 << (MAX_BIT_WIDTH - max_len));
        }
        else if (lit_freq[target] == 0 && XorShift::rand_double() < 0.5) {
            // 使っていないsymbolを1つ選んでlength=INFにする
            block.literal_code_lengths[target] = 0;
            new_kreft_value -= (1 << (MAX_BIT_WIDTH - old_len));
        }
        else {
            int type = XorShift::randn<3>();
            if (type == 0) {
                // decrease length by 1
                if (old_len > 1) {
                    block.literal_code_lengths[target]--;
                    new_kreft_value += (1 << (MAX_BIT_WIDTH - old_len));
                    body_length_diff -= lit_freq[target];
                }
            } else if (type == 1) {
                // swap with another
                int other = XorShift::randn(block.literal_code_lengths.size());
                while (other == target || block.literal_code_lengths[other] == 0) {
                    other = XorShift::randn(block.literal_code_lengths.size());
                }
                int other_len = block.literal_code_lengths[other];
                block.literal_code_lengths[target] = other_len;
                block.literal_code_lengths[other] = old_len;
                // no change in kreft_value
                body_length_diff += (other_len - old_len) * lit_freq[target];
                body_length_diff += (old_len - other_len) * lit_freq[other];
            } else { // type == 2
                // increase length by 1
                if (old_len < MAX_BIT_WIDTH) {
                    block.literal_code_lengths[target]++;
                    // Kreft value will decrease
                    new_kreft_value -= (1 << (MAX_BIT_WIDTH - old_len - 1));
                    body_length_diff += lit_freq[target];
                }
            }
        }

        int old_rle_part_len = RLE_part_code_length(old_lit_code_lengths, block.distance_code_lengths);
        int new_rle_part_len = RLE_part_code_length(block.literal_code_lengths, block.distance_code_lengths);
        int length_diff = body_length_diff + (new_rle_part_len - old_rle_part_len);

        double score_diff = length_diff + kreft_penalty(new_kreft_value, t) - kreft_penalty(kreft_value, t);

        if (score_diff < 0) {
        // if (score_diff <= 0 || XorShift::rand_double() < exp(-score_diff / (1.0 + t * 10.0))) {
            kreft_value = new_kreft_value;
            std::cout << "iter " << iter
                      << "   : " << (body_length_diff + (new_rle_part_len - old_rle_part_len))
                      <<     " " << double(kreft_value) / (1 << MAX_BIT_WIDTH) << std::endl;
        } else {
            block.literal_code_lengths = old_lit_code_lengths;
        }
    }
}