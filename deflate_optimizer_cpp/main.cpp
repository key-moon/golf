#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <memory>


struct Block {
    bool bfinal;
    virtual void dump_string(std::ostream& out) const = 0;
    virtual int bit_length() const = 0;
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
int num_bits_occupied_for_lit_code_fixed_huffman(int literal) {
    return literal <= 143 ? 8 : 9;
}
int num_bits_occupied_for_len_code_fixed_huffman(int length) {
    if (length <= 114) return 7 + num_additional_bits_for_len(length);
    else return 8 + num_additional_bits_for_len(length);
}
int num_bits_occupied_for_dist_code_fixed_huffman(int distance) {
    return 5 + num_additional_bits_for_dist(distance);
}

struct FixedHuffmanBlock : public Block {
    std::vector<Token> tokens;
    void dump_string(std::ostream& out) const {
        out << bfinal << ' ' << 0b01 << '\n';
        out << tokens.size() << '\n';
        for (int i = 0; i < tokens.size(); ++i) {
            out << tokens[i].get_string() << (i + 1 == tokens.size() ? "\n" : " ");
        }
    }
    int bit_length() const override {
        int length = 3;
        for (const auto& token : tokens) {
            if (token.type == Token::LITERAL) {
                length += num_bits_occupied_for_lit_code_fixed_huffman(token.literal);
            } else {
                length += num_bits_occupied_for_len_code_fixed_huffman(token.pair.length);
                length += num_bits_occupied_for_dist_code_fixed_huffman(token.pair.distance);
            }
        }
        length += num_bits_occupied_for_lit_code_fixed_huffman(256);
        return length;
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
};

struct DynamicHuffmanBlock : public Block {
    std::vector<int> literal_code_lengths;
    std::vector<int> distance_code_lengths;
    std::vector<Token> tokens;
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
    int bit_length() const override {
        throw std::runtime_error("Not implemented");
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
};

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

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <deflate_dump_file>\n";
        return 1;
    }
    std::string filepath = argv[1];
    std::ifstream infile(filepath);
    if (!infile.is_open()) {
        std::cerr << "Error opening file: " << filepath << "\n";
        return 1;
    }
    int length = 0;
    while (infile.peek() != EOF) {
        auto block = load_block_from_stream(infile);
        block->dump_string(std::cout);
        length += block->bit_length();
        while (infile.peek() == '\n' || infile.peek() == ' ' || infile.peek() == '\r' || infile.peek() == '\t') {
            infile.get();
        }
    }
    std::cout << "Total bit length: " << length << "\n";
    return 0;
}
