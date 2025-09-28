#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"

int main(int argc, char** argv) {
    if (argc != 2 && argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <deflate_dump_file> [num_iter=10]\n";
        return 1;
    }
    std::string filepath = argv[1];
    std::ifstream infile(filepath);
    if (!infile.is_open()) {
        std::cerr << "Error opening file: " << filepath << "\n";
        return 1;
    }

    int num_iter = 10;
    if (argc == 3) {
        num_iter = std::stoi(argv[2]);
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
    std::cerr << "Total bit length (input): " << length << "\n";

    length = 0;
    std::vector<int> text;
    for(const auto& block : blocks) {
        if (auto* db = dynamic_cast<DynamicHuffmanBlock*>(block.get())) {
            optimize_huffman_tree(*db, text, true, num_iter);
        }
        block->dump_string(std::cout);
        auto block_text = block->get_string(text);
        text.insert(text.end(), block_text.begin(), block_text.end());
        length += block->bit_length();
    }
    std::cerr << "Total bit length (output): " << length << "\n";

    return 0;
}
