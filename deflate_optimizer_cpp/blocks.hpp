#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <memory>
#include <queue>

struct Block {
    bool bfinal;
    virtual void dump_string(std::ostream& out) const = 0;
    virtual int bit_length() const = 0;
    virtual std::vector<int> get_string(const std::vector<int>& context) const = 0;
};

struct Token {
    enum Type { LITERAL, COPY } type;
    union {
        unsigned char literal;
        struct { int length; int distance; } pair;
    };
    std::string get_string() const {
        if (type == LITERAL) {
            return "L " + std::to_string(static_cast<int>(literal));
        } else {
            return "M " + std::to_string(pair.length) + " " + std::to_string(pair.distance);
        }
    }
};

struct RLEEntry {
    int value;
    int count;
};

struct RLECode {
    enum Type { LITERAL, PREV_RUN, ZERO_RUN } type;
    int value; // literal value for LITERAL, run length for PREV_RUN and ZERO_RUN
    int num_additional_bits() const {
        if (type == LITERAL) return 0;
        else if (type == PREV_RUN) {
            if (3 <= value && value <= 6) return 2;
            else throw std::runtime_error("Invalid PREV_RUN length");
        } else { // ZERO_RUN
            if (value <= 10) return 3;
            else if (value <= 138) return 7;
            else throw std::runtime_error("Invalid ZERO_RUN length");
        }
    }
    int id() const {
        if(type == LITERAL) {
           return value;
        }
        else if (type == PREV_RUN) {
            return 16;
        }
        else { // ZERO_RUN
            return (value <= 10) ? 17 : 18;
        }
    }
};

std::vector<int> compute_huff_code_lengths_from_frequencies(const std::vector<int>& frequencies) {
    // construct from frequencies
    // using a priority queue (min-heap)
    // use above reference-implementation
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> pq;
    std::vector<int> parents(frequencies.size(), -1);
    for (int i = 0; i < frequencies.size(); ++i) {
        if (frequencies[i] > 0) {
            pq.emplace(frequencies[i], i);
        }
    }
    while (pq.size() > 1) {
        auto [freq1, idx1] = pq.top();
        pq.pop();
        auto [freq2, idx2] = pq.top();
        pq.pop();
        parents[idx1] = parents.size();
        parents[idx2] = parents.size();
        pq.emplace(freq1 + freq2, parents.size());
        parents.emplace_back(-1);
    }
    std::vector<int> code_lengths(parents.size(), 0);
    for(int i = parents.size() - 1; i >= 0; --i) {
        if (parents[i] != -1) {
            code_lengths[i] = code_lengths[parents[i]] + 1;
        }
    }
    code_lengths.resize(frequencies.size());
    return code_lengths;
}

std::vector<RLECode> convert_RLEEntry_to_RLECode(const RLEEntry& entry) {
    // Note: This conversion is not optimal.
    std::vector<RLECode> res;
    if(entry.value == 0) {
        int run_length = entry.count;
        while (run_length > 0) {
            if (run_length >= 3) {
                int length = std::min(run_length, 138);
                res.push_back({RLECode::ZERO_RUN, length});
                run_length -= length;
            } else {
                res.push_back({ RLECode::LITERAL, entry.value });
                run_length--;
            }
        }
    } else {
        res.push_back({ RLECode::LITERAL, entry.value });
        int run_length = entry.count - 1;
        while (run_length > 0) {
            if (run_length >= 6) {
                res.push_back({ RLECode::PREV_RUN, 6 });
                run_length -= 6;
            } else if (run_length >= 3) {
                res.push_back({ RLECode::PREV_RUN, run_length });
                run_length = 0;
            } else {
                res.push_back({ RLECode::LITERAL, entry.value });
                run_length--;
            }
        }
    }
    return res;
}

Token read_one_token(std::istream& in) {
    char type;
    in >> type;
    if (type == 'L') {
        int literal;
        in >> literal;
        Token tok = 
            { Token::LITERAL, .literal = static_cast<unsigned char>(literal) };
        return tok;
    } else if (type == 'M') {
        int length, distance;
        in >> length >> distance;
        Token tok = { Token::COPY, .pair = { length, distance } };
        return tok;
    } else {
        throw std::runtime_error("Invalid token type");
    }
}

int convert_length_value_to_code(int length) {
    if (length <= 10) return 257 + (length - 3);
    else if (length <= 18) return 265 + (length - 11) / 2;
    else if (length <= 34) return 269 + (length - 19) / 4;
    else if (length <= 66) return 273 + (length - 35) / 8;
    else if (length <= 130) return 277 + (length - 67) / 16;
    else if (length <= 257) return 281 + (length - 131) / 32;
    else if (length == 258) return 285;
    else throw std::runtime_error("Invalid length");
}
int convert_distance_value_to_code(int distance) {
    if (distance <= 4) return distance - 1;
    else if (distance <= 8) return 4 + (distance - 5) / 2;
    else if (distance <= 16) return 6 + (distance - 9) / 4;
    else if (distance <= 32) return 8 + (distance - 17) / 8;
    else if (distance <= 64) return 10 + (distance - 33) / 16;
    else if (distance <= 128) return 12 + (distance - 65) / 32;
    else if (distance <= 256) return 14 + (distance - 129) / 64;
    else if (distance <= 512) return 16 + (distance - 257) / 128;
    else if (distance <= 1024) return 18 + (distance - 513) / 256;
    else if (distance <= 2048) return 20 + (distance - 1025) / 512;
    else if (distance <= 4096) return 22 + (distance - 2049) / 1024;
    else if (distance <= 8192) return 24 + (distance - 4097) / 2048;
    else if (distance <= 16384) return 26 + (distance - 8193) / 4096;
    else if (distance <= 32768) return 28 + (distance - 16385) / 8192;
    else throw std::runtime_error("Invalid distance");
}
int num_additional_bits_for_len(int length) {
    if (length <= 10) return 0;
    else if (length <= 18) return 1;
    else if (length <= 34) return 2;
    else if (length <= 66) return 3;
    else if (length <= 130) return 4;
    else if (length <= 257) return 5;
    else if (length == 258) return 0;
    else throw std::runtime_error("Invalid length");
}
int num_additional_bits_for_dist(int distance) {
    if (distance <= 4) return 0;
    else if (distance <= 8) return 1;
    else if (distance <= 16) return 2;
    else if (distance <= 32) return 3;
    else if (distance <= 64) return 4;
    else if (distance <= 128) return 5;
    else if (distance <= 256) return 6;
    else if (distance <= 512) return 7;
    else if (distance <= 1024) return 8;
    else if (distance <= 2048) return 9;
    else if (distance <= 4096) return 10;
    else if (distance <= 8192) return 11;
    else if (distance <= 16384) return 12;
    else if (distance <= 32768) return 13;
    else throw std::runtime_error("Invalid distance");
}

std::vector<int> CL_CODE_ORDER = {
    16, 17, 18, 0, 8, 7, 9, 6,
    10, 5, 11, 4, 12, 3, 13, 2,
    14, 1, 15
};

std::vector<RLEEntry> length_RLE(const std::vector<int>& vec) {
    std::vector<RLEEntry> res;
    int prev = -1;
    int run_length = 0;
    for(int i = 0; i < vec.size() + 1; ++i) {
        int value = (i == vec.size()) ? -1 : vec[i];
        if (value == prev) {
            run_length++;
        } else {
            if (prev != -1 ) {
                res.push_back({prev, run_length});
            }
            prev = value;
            run_length = 1;
        }
    }
    return res;
}

struct CompressedBlock : public Block {
    std::vector<Token> tokens;
    virtual int get_literal_code_length(int literal_code) const = 0;
    virtual int get_distance_code_length(int distance_code) const = 0;
};
    

std::vector<RLECode> compute_RLE_encoded_representation(const std::vector<int>& literal_code_lengths, const std::vector<int>& distance_code_lengths) {
    // Note: This run-length encoding is not optimal.
    // Each run-length encoded symbol will be compressed using huffman codes, so acutually we should consider it.
    std::vector<int> concat = literal_code_lengths;
    concat.insert(concat.end(), distance_code_lengths.begin(), distance_code_lengths.end());
    auto rle_entries = length_RLE(concat);
    std::vector<RLECode> rle_codes;
    for (const auto& entry : rle_entries) {
        auto codes = convert_RLEEntry_to_RLECode(entry);
        rle_codes.insert(rle_codes.end(), codes.begin(), codes.end());
    }
    return rle_codes;
}

struct StoredBlock : public Block {
    std::vector<int> data;
    void dump_string(std::ostream& out) const {
        out << bfinal << ' ' << 0b00 << '\n';
        out << data.size() << '\n';
        for (size_t i = 0; i < data.size(); ++i) {
            out << data[i] << (i + 1 == data.size() ? "\n" : " ");
        }
    }
    int bit_length() const override {
        // Acutually the data after bfinal and btype is byte-aligned.
        // Here we just return the bit length as if it were not aligned.
        return 3 + 16 + 16 + data.size() * 8;
    }
    std::vector<int> get_string(const std::vector<int>& context) const override {
        return data;
    }
    static StoredBlock load_from_stream(std::istream& in) {
        StoredBlock block;
        size_t len;
        in >> len;
        block.data.resize(len);
        for (size_t i = 0; i < len; ++i) {
            int byte_val;
            in >> byte_val;
            block.data[i] = static_cast<unsigned char>(byte_val);
        }
        return block;
    }
};

struct DynamicHuffmanBlock;

struct FixedHuffmanBlock : public CompressedBlock {
    void dump_string(std::ostream& out) const {
        out << bfinal << ' ' << 0b01 << '\n';
        out << tokens.size() << '\n';
        for (int i = 0; i < tokens.size(); ++i) {
            out << tokens[i].get_string() << (i + 1 == tokens.size() ? "\n" : " ");
        }
    }
    int bit_length() const override {
        // std::cout << "num factors: " << tokens.size() << std::endl;
        int length = 3;
        for (const auto& token : tokens) {
            if (token.type == Token::LITERAL) {
                length += get_literal_code_length(token.literal);
            } else {
                int lit_code = convert_length_value_to_code(token.pair.length);
                length += get_literal_code_length(lit_code);
                length += num_additional_bits_for_len(token.pair.length);
                int dist_code = convert_distance_value_to_code(token.pair.distance);
                length += get_distance_code_length(dist_code);
                length += num_additional_bits_for_dist(token.pair.distance);
            }
        }
        length += get_literal_code_length(256);
        return length;
    }
    std::vector<int> get_string(const std::vector<int>& context) const override {
        std::vector<int> res;
        for (const auto& token : tokens) {
            if (token.type == Token::LITERAL) {
                res.push_back(token.literal);
            } else {
                int start = res.size() - token.pair.distance;
                for (int i = 0; i < token.pair.length; ++i) {
                    if (start + i >= 0 && start + i < res.size()) {
                        res.push_back(res[start + i]);
                    } else if (start + i >= 0 && start + i < context.size()) {
                        res.push_back(context[start + i]);
                    } else {
                        throw std::runtime_error("COPY distance out of bounds");
                    }
                }
            }
        }
        return res;
    }
    int get_literal_code_length(int literal_code) const override {
        if (literal_code <= 143) return 8;
        else if (literal_code <= 255) return 9;
        else if (literal_code <= 279) return 7;
        else if (literal_code <= 287) return 8;
        else throw std::runtime_error("Invalid literal");
    }
    int get_distance_code_length(int distance_code) const override {
        return 5;
    }
    static FixedHuffmanBlock load_from_stream(std::istream& in) {
        FixedHuffmanBlock block;
        size_t len;
        in >> len;
        block.tokens.resize(len);
        for (size_t i = 0; i < len; ++i) {
            block.tokens[i] = read_one_token(in);
        }
        return block;
    }
    DynamicHuffmanBlock to_dynamic_huffman_block() const;
};

struct DynamicHuffmanBlock : public CompressedBlock {
    std::vector<int> literal_code_lengths;
    std::vector<int> distance_code_lengths;
    void dump_string(std::ostream& out) const {
        out << bfinal << ' ' << 0b10 << '\n';
        out << literal_code_lengths.size() << '\n';
        for (size_t i = 0; i < literal_code_lengths.size(); ++i) {
            out << literal_code_lengths[i] << (i + 1 == literal_code_lengths.size() ? "\n" : " ");
        }
        out << distance_code_lengths.size() << '\n';
        for (size_t i = 0; i < distance_code_lengths.size(); ++i) {
            out << distance_code_lengths[i] << (i + 1 == distance_code_lengths.size() ? "\n" : " ");
        }
        out << tokens.size() << '\n';
        for (int i = 0; i < tokens.size(); ++i) {
            out << tokens[i].get_string() << (i + 1 == tokens.size() ? "\n" : " ");
        }
    }
    auto get_cl_code_lengths() const {
        std::vector<RLECode> rle_codes = compute_RLE_encoded_representation(literal_code_lengths, distance_code_lengths);
        std::vector<int> cl_frequencies(19, 0);
        for (const auto& code : rle_codes) {
            cl_frequencies[code.id()]++;
        }
        /*
        std::cout << " ----------------------------- " << std::endl;
        for(auto & code : rle_codes) {
            std::cout << "RLE code: type=" << (code.type == RLECode::LITERAL ? "LITERAL" : (code.type == RLECode::PREV_RUN ? "PREV_RUN" : "ZERO_RUN")) 
                      << ", value=" << code.value 
                      << ", id=" << code.id() 
                      << ", additional_bits=" << code.num_additional_bits() 
                      << std::endl;
        }
        auto cl_freq = compute_huff_code_lengths_from_frequencies(cl_frequencies);
        for(int i = 0; i < cl_freq.size(); ++i) {
            std::cout << "cl_freq[" << i << "] = " << cl_freq[i] << std::endl;
        }
        std::cout << "----------------------------- " << std::endl;
        */
        return compute_huff_code_lengths_from_frequencies(cl_frequencies);
    }
    int bit_length() const override {
        // std::cout << "num factors: " << tokens.size() << std::endl;
        int length = 3; // bfinal + btype
        // HLIT, HDIST, HCLEN
        length += 5 + 5 + 4;
        auto cl_code_lengths = get_cl_code_lengths();
        int hclen = 0;
        for (int i = 18; i >= 0; --i) {
            if (cl_code_lengths[CL_CODE_ORDER[i]] > 0) {
                hclen = i + 1;
                break;
            }
        }
        length += hclen * 3;
        std::vector<RLECode> rle_codes = compute_RLE_encoded_representation(literal_code_lengths, distance_code_lengths);
        for (auto& code : rle_codes) {
            length += cl_code_lengths[code.id()];
            length += code.num_additional_bits();
        }
        // body
        for(auto tok : tokens) {
            if (tok.type == Token::LITERAL) {
                length += literal_code_lengths[tok.literal];
            } else { // COPY
                int lit_code = convert_length_value_to_code(tok.pair.length);
                int distance_code = convert_distance_value_to_code(tok.pair.distance);
                length += literal_code_lengths[lit_code];
                length += num_additional_bits_for_len(tok.pair.length);
                length += distance_code_lengths[distance_code];
                length += num_additional_bits_for_dist(tok.pair.distance);
            }
        }
        length += get_literal_code_length(256);
        return length;
    }
    std::vector<int> get_string(const std::vector<int>& context) const override {
        std::vector<int> res;
        for (const auto& token : tokens) {
            if (token.type == Token::LITERAL) {
                res.push_back(token.literal);
            } else {
                int start = res.size() - token.pair.distance;
                for (int i = 0; i < token.pair.length; ++i) {
                    if (start + i >= 0 && start + i < res.size()) {
                        res.push_back(res[start + i]);
                    } else if (start + i >= 0 && start + i < context.size()) {
                        res.push_back(context[start + i]);
                    } else {
                        throw std::runtime_error("COPY distance out of bounds");
                    }
                }
            }
        }
        return res;
    }
    int get_literal_code_length(int literal_code) const override {
        return (literal_code >= literal_code_lengths.size() || literal_code_lengths[literal_code] == 0)
                ? 1e9
                : literal_code_lengths[literal_code];
    }
    int get_distance_code_length(int distance_code) const override {
        return (distance_code >= distance_code_lengths.size() || distance_code_lengths[distance_code] == 0)
                ? 1e9
                : distance_code_lengths[distance_code];
    }
    static DynamicHuffmanBlock load_from_stream(std::istream& in) {
        DynamicHuffmanBlock block;
        size_t hlit, hdist;
        in >> hlit;
        block.literal_code_lengths.resize(hlit);
        for (size_t i = 0; i < hlit; ++i) {
            in >> block.literal_code_lengths[i];
        }
        in >> hdist;
        block.distance_code_lengths.resize(hdist);
        for (size_t i = 0; i < hdist; ++i) {
            in >> block.distance_code_lengths[i];
        }
        size_t len;
        in >> len;
        block.tokens.resize(len);
        for (size_t i = 0; i < len; ++i) {
            block.tokens[i] = read_one_token(in);
        }
        return block;
    }
    FixedHuffmanBlock to_fixed_huffman_block() const {
        FixedHuffmanBlock block;
        block.bfinal = bfinal;
        block.tokens = tokens;
        return block;
    }
};

DynamicHuffmanBlock FixedHuffmanBlock::to_dynamic_huffman_block() const {
    DynamicHuffmanBlock block;
    block.bfinal = bfinal;
    block.tokens = tokens;
    block.literal_code_lengths.resize(288, 0);
    for (int i = 0; i <= 143; ++i) block.literal_code_lengths[i] = 8;
    for (int i = 144; i <= 255; ++i) block.literal_code_lengths[i] = 9;
    for (int i = 256; i <= 279; ++i) block.literal_code_lengths[i] = 7;
    for (int i = 280; i <= 287; ++i) block.literal_code_lengths[i] = 8;
    block.distance_code_lengths.resize(32, 0);
    for (int i = 0; i <= 31; ++i) block.distance_code_lengths[i] = 5;
    return block;
}

static std::unique_ptr<Block> load_block_from_stream(std::istream& in) {
    int bfinal_int, btype;
    in >> bfinal_int >> btype;
    bool bfinal = (bfinal_int != 0);
    if (btype == 0b00) {
        auto blk = std::make_unique<StoredBlock>(StoredBlock::load_from_stream(in));
        blk->bfinal = bfinal;
        return blk;
    } else if (btype == 0b01) {
        auto blk = std::make_unique<FixedHuffmanBlock>(FixedHuffmanBlock::load_from_stream(in));
        blk->bfinal = bfinal;
        return blk;
    } else if (btype == 0b10) {
        auto blk = std::make_unique<DynamicHuffmanBlock>(DynamicHuffmanBlock::load_from_stream(in));
        blk->bfinal = bfinal;
        return blk;
    } else {
        throw std::runtime_error("Unsupported block type");
    }
}
