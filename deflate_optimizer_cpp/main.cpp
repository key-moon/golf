#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <memory>


struct Block {
    bool bfinal;
    virtual void dump_string(std::ostream& out) = 0;
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
    void dump_string(std::ostream& out) {
        out << bfinal << ' ' << 0b00 << '\n';
        out << data.size() << '\n';
        for (size_t i = 0; i < data.size(); ++i) {
            out << data[i] << (i + 1 == data.size() ? "\n" : " ");
        }
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

struct FixedHuffmanBlock : public Block {
    std::vector<Token> tokens;
    void dump_string(std::ostream& out) {
        out << bfinal << ' ' << 0b01 << '\n';
        out << tokens.size() << '\n';
        for (int i = 0; i < tokens.size(); ++i) {
            out << tokens[i].get_string() << (i + 1 == tokens.size() ? "\n" : " ");
        }
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
    void dump_string(std::ostream& out) {
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
    while (infile.peek() != EOF) {
        auto block = load_block_from_stream(infile);
        block->dump_string(std::cout);
        while (infile.peek() == '\n' || infile.peek() == ' ' || infile.peek() == '\r' || infile.peek() == '\t') {
            infile.get();
        }
    }
    return 0;
}
