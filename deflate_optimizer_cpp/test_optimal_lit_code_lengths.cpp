#include <iostream>
#include <string>
#include <vector>
#include <chrono>

#include "optimal_lit_code_lengths.hpp"

namespace {

Token make_literal(int value) {
    Token token{};
    token.type = Token::LITERAL;
    token.literal = static_cast<unsigned char>(value);
    return token;
}

Token make_copy(int length, int distance) {
    Token token{};
    token.type = Token::COPY;
    token.pair.length = length;
    token.pair.distance = distance;
    return token;
}

DynamicHuffmanBlock base_block() {
    DynamicHuffmanBlock block;
    block.cl_code_lengths.assign(19, 5);
    block.cl_code_lengths[0] = 4;
    block.cl_code_lengths[16] = 6;
    block.cl_code_lengths[17] = 7;
    block.cl_code_lengths[18] = 8;
    return block;
}

bool is_valid_kraft_sum(const std::vector<int>& lengths, int max_bit_width) {
    const int target = 1 << max_bit_width;
    int sum = 0;
    for (int length : lengths) {
        if (length == 0) {
            continue;
        }
        if (length < 0 || length > max_bit_width) {
            return false;
        }
        sum += 1 << (max_bit_width - length);
    }
    return sum == target;
}

bool run_case(const std::string& name, const DynamicHuffmanBlock& original, int max_bit_width = 9) {
    auto slow_block = original;
    auto fast_block = original;

    std::cout << "Running test case: " << name << std::endl;
    std::cout << "Running slow..." << std::endl;
    auto time_start = std::chrono::high_resolution_clock::now();
    optimize_lit_code_huffman_slow(slow_block, max_bit_width);
    auto time_end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(time_end - time_start).count();
    std::cout << "Slow optimization took " << duration << " [ms]" << std::endl;
    std::cout << "Running fast..." << std::endl;
    time_start = std::chrono::high_resolution_clock::now();
    optimize_lit_code_huffman_fast(fast_block, max_bit_width);
    time_end = std::chrono::high_resolution_clock::now();
    duration = std::chrono::duration_cast<std::chrono::milliseconds>(time_end - time_start).count();
    std::cout << "Fast optimization took " << duration << " [ms]" << std::endl;

    bool ok = true;
    if (slow_block.literal_code_lengths != fast_block.literal_code_lengths) {
        std::cerr << name << ": slow/fast literal code lengths differ" << std::endl;
        std::cerr << "slow:";
        for (int v : slow_block.literal_code_lengths) {
            std::cerr << ' ' << v;
        }
        std::cerr << std::endl;
        std::cerr << "fast:";
        for (int v : fast_block.literal_code_lengths) {
            std::cerr << ' ' << v;
        }
        std::cerr << std::endl;
        std::cerr << "slow kraft ok: " << is_valid_kraft_sum(slow_block.literal_code_lengths, max_bit_width) << std::endl;
        std::cerr << "fast kraft ok: " << is_valid_kraft_sum(fast_block.literal_code_lengths, max_bit_width) << std::endl;
        std::cerr << "diff idx:";
        for (int idx = 0; idx < static_cast<int>(slow_block.literal_code_lengths.size()); ++idx) {
            if (slow_block.literal_code_lengths[idx] != fast_block.literal_code_lengths[idx]) {
                std::cerr << ' ' << idx;
            }
        }
        std::cerr << std::endl;
        ok = false;
    }
    if (slow_block.literal_code_lengths.empty()) {
        std::cerr << name << ": literal_code_lengths is empty" << std::endl;
        ok = false;
    }
    if (!is_valid_kraft_sum(slow_block.literal_code_lengths, max_bit_width)) {
        std::cerr << name << ": literal_code_lengths violates Kraft equality" << std::endl;
        ok = false;
    }
    return ok;
}

bool basic_literals() {
    auto block = base_block();
    block.tokens = {
        make_literal('A'),
        make_literal('A'),
        make_literal('B'),
        make_literal('B'),
        make_literal('C'),
        make_literal('D'),
        make_literal('D'),
    };
    return run_case("basic_literals", block, 7);
}

bool mix_with_copy_tokens() {
    auto block = base_block();
    block.tokens = {
        make_literal('A'),
        make_literal('B'),
        make_copy(3, 1),
        make_literal('C'),
        make_copy(4, 2),
        make_literal('D'),
    };
    return run_case("mix_with_copy_tokens", block, 9);
}

bool wide_alphabet() {
    auto block = base_block();
    block.tokens.clear();
    for (int i = 0; i < 26; ++i) {
        block.tokens.push_back(make_literal('a' + i));
    }
    block.tokens.push_back(make_copy(5, 4));
    block.tokens.push_back(make_copy(6, 8));
    return run_case("wide_alphabet", block, 9);
}

} // namespace

int main() {
    std::vector<std::pair<std::string, bool (*)()>> tests = {
        {"basic_literals", basic_literals},
        {"mix_with_copy_tokens", mix_with_copy_tokens},
        {"wide_alphabet", wide_alphabet},
    };

    bool all_ok = true;
    for (const auto& [name, fn] : tests) {
        if (!fn()) {
            all_ok = false;
        } else {
            std::cout << "[ok] " << name << std::endl;
        }
    }

    if (!all_ok) {
        std::cerr << "Some optimal literal code length tests failed" << std::endl;
        return 1;
    }
    std::cout << "All optimal literal code length tests passed" << std::endl;
    return 0;
}
