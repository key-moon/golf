#include "blocks.hpp"
#include "optimal_parsing.hpp"

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
    longest_greedy_parse(blocks);
    // optimal_parse(blocks);
    length = 0;
    for(const auto& block : blocks) {
        length += block->bit_length();
    }
    std::cout << "Total bit length (optimal parsing): " << length << "\n";

    return 0;
}
