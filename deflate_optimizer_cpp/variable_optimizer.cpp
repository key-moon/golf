#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"
#include "variable.hpp"
#include "variable_optimizer.hpp"

int main(int argc, char** argv) {
    if (argc != 3 && argc != 4 && argc != 5) {
        std::cerr << "Usage: " << argv[0] << " <deflate_dump_file> <variable_dump_file> [num_iter=10] [max_num_round=5]\n";
        return 1;
    }
    std::string filepath = argv[1];
    std::ifstream infile(filepath);
    if (!infile.is_open()) {
        std::cerr << "Error opening file: " << filepath << "\n";
        return 1;
    }

    std::string var_filepath = argv[2];
    std::ifstream varfile(var_filepath);
    if (!varfile.is_open()) {
        std::cerr << "Error opening file: " << var_filepath << "\n";
        return 1;
    }

    int num_iter = 5;
    if (argc >= 4) {
        num_iter = std::stoi(argv[3]);
    }

    int max_num_round = 10;
    if (argc == 5) {
        max_num_round = std::stoi(argv[4]);
    }

    std::vector<std::unique_ptr<Block>> blocks;
    int num_factors = 0;
    int length = 0;
    while (infile.peek() != EOF) {
        auto block = load_block_from_stream(infile);
        length += block->bit_length();
        while (infile.peek() == '\n' || infile.peek() == ' ' || infile.peek() == '\r' || infile.peek() == '\t') {
            infile.get();
        }
        blocks.push_back(std::move(block));
    }
    std::cerr << "Total bit length (input): " << length << "\n";

    std::vector<Variable> variables = load_variables_from_stream(varfile);

    if (blocks.size() != 1) {
        std::cerr << "Warning: variable optimization is only supported for single block deflate data. Skipping variable optimization.\n";
        for(const auto& block : blocks) {
            block->dump_string(std::cout);
        }
        return 0;
    }

    if (auto* db = dynamic_cast<DynamicHuffmanBlock*>(blocks[0].get())) {
        auto block = *db;
        for (int i = 0; i < max_num_round; ++i) {
            auto before_block = block;
            auto before_vars = variables;
            int before = block.bit_length();
            // std::cerr << "Optimizing variables..." << std::endl;
            auto variable_to_new_literal_mapping = optimize_variables(block, variables);
            replace_and_recompute_parsing(block, variables, variable_to_new_literal_mapping);
            // std::cerr << "Optimizing Huffman tree..." << std::endl;
            optimize_huffman_tree(block, {}, num_iter);
            // std::cerr << "Done." << std::endl;
            int after = block.bit_length();
            std::cerr << "Round " << i << ": " << before << " -> " << after << "\n";
            if (before <= after) {
                std::cerr << "No improvement, stop optimizing this block\n";
                block = before_block;
                variables = before_vars;
                break;
            }
            else {
                std::cerr << "Improved!\n";
            }
        }
        block.dump_string(std::cout);
        std::cerr << "Total bit length (output): " << block.bit_length() << "\n";
    } else {
        std::cerr << "Warning: variable optimization is only supported for dynamic Huffman blocks. Skipping variable optimization.\n";
        for(const auto& block : blocks) {
            block->dump_string(std::cout);
        }
        return 0;
    }

    return 0;
}
