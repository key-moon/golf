#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"
#include "variable.hpp"
#include "variable_optimizer.hpp"

// variable optimizerにブロック分割機能をつけただけ
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

    length = 0;

    if (blocks.size() != 1) {
        std::cerr << "Warning: variable optimization is only supported for single block deflate data. Skipping variable optimization.\n";
        for(const auto& block : blocks) {
            block->dump_string(std::cout);
        }
        return 0;
    }

    auto opt_fn = [&](DynamicHuffmanBlock& db, std::vector<Variable>& vars) {
        for (int i = 0; i < max_num_round; ++i) {
            auto before_block = db;
            auto before_vars = vars;
            int before = db.bit_length();
            // std::cerr << "Optimizing variables..." << std::endl;
            optimize_variables(db, vars, {});
            // std::cerr << "Optimizing Huffman tree..." << std::endl;
            optimize_huffman_tree(db, {}, true, num_iter);
            // std::cerr << "Done." << std::endl;
            int after = db.bit_length();
            if (before <= after) {
                db = before_block;
                vars = before_vars;
                break;
            }
        }
    };

    auto vars_pop = [&](const std::vector<Variable>& variables, int pos) {
        std::vector<Variable> res;
        for (const auto& var : variables) {
            std::vector<int> new_occurrences;
            for (const auto& occ : var.occurrences) {
                if (occ + var.name.size() <= pos) {
                    new_occurrences.push_back(occ);
                }
            }
            if (!new_occurrences.empty()) {
                Variable new_var;
                new_var.name = var.name;
                new_var.occurrences = new_occurrences;
                res.push_back(new_var);
            }
        }
        return res;
    };

    for(const auto& block : blocks) {
        if (auto* db = dynamic_cast<DynamicHuffmanBlock*>(block.get())) {

            opt_fn(*db, variables);

            std::tuple<int, DynamicHuffmanBlock, FixedHuffmanBlock> best = {
                db->bit_length(),
                *db,
                FixedHuffmanBlock()
            };
            std::cerr << "Current bit length: " << db->bit_length() << std::endl;

            auto text = block->get_string({});
            for (int spl = text.size() - 1; spl >= 1; --spl) {
                std::cerr << "Attempt: " << spl << " / " << text.size() << std::endl;
                auto [block1, block2] = db->split_at_position(spl);

                std::vector<Variable> vars1 = vars_pop(variables, spl);

                opt_fn(block1, vars1);

                int len_sum = block1.bit_length() + block2.bit_length();
                std::cerr << "Total length: " << len_sum << " / " << db->bit_length() << std::endl;
                if (std::get<0>(best) > len_sum) {
                    std::cerr << "Improved! " << std::get<0>(best) << " -> " << len_sum << std::endl;
                    best = std::make_tuple(len_sum, block1, block2);
                }
            }

            if (std::get<0>(best) < db->bit_length()) {
                std::cerr << "Splitting into two blocks improved! " << db->bit_length() << " -> " << std::get<0>(best) << std::endl;
                std::get<1>(best).dump_string(std::cout);
                std::get<2>(best).dump_string(std::cout);
                length += std::get<0>(best);
                continue;
            }
            else {
                block->dump_string(std::cout);
                length += block->bit_length();
            }
        }
    }
    std::cerr << "Total bit length (output): " << length << "\n";

    return 0;
}
