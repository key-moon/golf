#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"

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
    std::vector<std::unique_ptr<Block>> blocks;
    int num_factors = 0;
    int length = 0;
    while (infile.peek() != EOF) {
        auto block = load_block_from_stream(infile);
        // block->dump_string(std::cout);
        length += block->bit_length();
        while (infile.peek() == '\n' || infile.peek() == ' ' || infile.peek() == '\r' || infile.peek() == '\t') {
            infile.get();
        }
        blocks.push_back(std::move(block));
    }
    std::cout << "Total bit length (input): " << length << "\n";
    // optimal_parse(blocks);

    std::ofstream outfile(filepath + ".optimized");
    if (!outfile.is_open()) {
        std::cerr << "Error opening file for writing: " << filepath + ".optimized" << "\n";
        return 1;
    }

    length = 0;
    for(const auto& block : blocks) {
        if (auto* db = dynamic_cast<DynamicHuffmanBlock*>(block.get())) {
            optimize_huffman_tree(*db);
            block->dump_string(std::cout);
            block->dump_string(outfile);
        }
        length += block->bit_length();
    }
    std::cout << "Total bit length (output): " << length << "\n";

    return 0;
}
