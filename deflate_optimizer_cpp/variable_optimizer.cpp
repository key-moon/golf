#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"
#include "variable.hpp"
#include "variable_optimizer.hpp"

int main(int argc, char** argv) {
    if (argc != 3 && argc != 4 && argc != 5) {
        std::cerr << "Usage: " << argv[0] << " <deflate_dump_file> <variable_dump_file> [num_iter=10] [max_num_round=10]\n";
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
    std::vector<std::vector<bool>> var_dependency = load_dependency_matrix_from_stream(varfile, variables.size());
    std::cerr << "Variables:\n";
    for (int i = 0; i < variables.size(); ++i) {
        for (int j = 0; j < variables.size(); ++j) {
            if (!var_dependency[i][j] && i != j && variables[i].name.size() == 1 && variables[j].name.size() == 1) {
                std::cerr << "Variable " << i << " (" << variables[i].name << ") does not depend on Variable " << j << " (" << variables[j].name << ")\n";
            }
        }
    }

    if (blocks.size() != 1) {
        std::cerr << "Warning: variable optimization is only supported for single block deflate data. Skipping variable optimization.\n";
        for(const auto& block : blocks) {
            block->dump_string(std::cout);
        }
        return 0;
    }


    if (auto* db = dynamic_cast<DynamicHuffmanBlock*>(blocks[0].get())) {


        int best_length = db->bit_length();
        auto best_block = *db;
        auto best_variables = variables;

        auto trial = [&](const DynamicHuffmanBlock& _block, const std::vector<Variable>& _variables, FreqCount freq_count, TieBreak tie_break) {
            auto block = _block;
            auto variables = _variables;
            int before = block.bit_length();
            auto variable_to_new_literal_mapping = optimize_variables(block, variables, var_dependency, freq_count, tie_break, VariableAssignment::Greedy);
            replace_and_recompute_parsing(block, variables, variable_to_new_literal_mapping);
            optimize_huffman_tree(block, {}, true, num_iter);
            int after = block.bit_length();
            if (before <= after) {
                return std::make_tuple(false, _block, _variables);
            }
            else {
                if (after < best_length) {
                    best_length = after;
                    best_block = block;
                    best_variables = variables;
                }
                return std::make_tuple(true, block, variables);
            }
        };


        // 改善する限り回す
        std::vector<std::pair<DynamicHuffmanBlock, std::vector<Variable>>> cands;
        cands.push_back({*db, variables});
        for (int i = 0; i < max_num_round; ++i) {
            std::vector<std::pair<DynamicHuffmanBlock, std::vector<Variable>>> new_cands;
            for (auto [cand_block, cand_vars] : cands) {
                auto res1 = trial(cand_block, cand_vars, FreqCount::NumNonVarAsLiteral, TieBreak::NonVarFreq);
                auto res2 = trial(cand_block, cand_vars, FreqCount::NumNonVarAsLiteral, TieBreak::BFS);
                if (std::get<0>(res1)) {
                    new_cands.push_back({std::get<1>(res1), std::get<2>(res1)});
                }
                if (std::get<0>(res2)) {
                    new_cands.push_back({std::get<1>(res2), std::get<2>(res2)});
                }
            }
            if (new_cands.size() == 0) {
                std::cerr << "No improvement in this round. Stopping.\n";
                break;
            }
            std::swap(cands, new_cands);
            std::cerr << "Round " << i << " completed with " << cands.size() << " candidates.\n";
        }

        /* 旧バージョンの実装（全探索していないので早いが相対的に弱い）
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
        */

        std::cerr << "Total bit length (output): " << best_block.bit_length() << "\n";
        std::cerr << "Final cl-code lengths optimization...\n";
        std::cerr << "OLD cl code lengths: ";
        for (auto l : best_block.cl_code_lengths) {
            std::cerr << l << " ";
        }
        std::cerr << std::endl;
        best_block.cl_code_lengths = get_optimal_cl_code_lengths(best_block.literal_code_lengths, best_block.distance_code_lengths);
        std::cerr << "NEW cl code lengths: ";
        for (auto l : best_block.cl_code_lengths) {
            std::cerr << l << " ";
        }
        std::cerr << std::endl;
        std::cerr << "Total bit length (output): " << best_block.bit_length() << "\n";


        best_block.dump_string(std::cout);
        std::cerr << "Total bit length (output): " << best_block.bit_length() << "\n";
    } else {
        std::cerr << "Warning: variable optimization is only supported for dynamic Huffman blocks. Skipping variable optimization.\n";
        for(const auto& block : blocks) {
            block->dump_string(std::cout);
        }
        return 0;
    }

    return 0;
}
