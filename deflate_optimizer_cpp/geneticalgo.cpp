#include <unordered_set>

#include "blocks.hpp"
#include "optimal_parsing.hpp"
#include "optimizer.hpp"
#include "variable.hpp"
#include "variable_optimizer.hpp"


std::vector<std::vector<int>> INITIAL_CL_CODE_LENGTHS = {
    {0,0,0,5,3,2,0,0,2,0,0,0,0,0,0,0,2,5,4},
    {2,0,5,5,5,4,1,0,0,0,0,0,0,0,0,0,0,4,5},
    {0,0,0,4,4,2,3,0,2,0,0,0,0,0,0,0,3,4,4},
    {1,0,5,0,3,4,2,0,0,0,0,0,0,0,0,0,0,0,5},
    {0,0,6,6,4,2,5,4,2,0,0,0,0,0,0,0,3,3,4},
    {3,0,0,5,3,0,2,0,3,0,0,0,0,0,0,0,2,5,4},
    {0,0,0,6,0,1,6,0,2,0,0,0,0,0,0,0,3,5,4},
    {5,0,5,5,5,2,0,0,1,0,0,0,0,0,0,0,0,4,4},
    {0,0,5,0,3,3,0,1,0,0,0,0,0,0,0,0,3,5,4},
    {1,0,5,5,5,3,2,0,0,0,0,0,0,0,0,0,0,0,5},
    {1,0,5,0,3,4,0,2,0,0,0,0,0,0,0,0,0,0,5},
    {2,0,0,6,5,2,2,0,4,0,0,0,0,0,0,0,4,6,4},
    {0,0,0,6,6,2,5,0,1,0,0,0,0,0,0,0,3,5,5},
    {5,0,5,0,2,4,0,1,0,0,0,0,0,0,0,0,0,4,4},
    {0,0,0,5,3,3,0,1,0,0,0,0,0,0,0,0,5,3,4},
    {0,0,5,5,5,2,0,0,1,0,0,0,0,0,0,0,0,3,5},
    {3,0,0,4,3,2,0,0,3,0,0,0,0,0,0,0,2,0,4},
    {1,0,0,5,4,0,2,0,0,0,0,0,0,0,0,0,3,0,5},
    {1,0,5,5,5,3,0,2,0,0,0,0,0,0,0,0,0,0,5},
    {0,0,0,5,4,5,2,0,2,0,0,0,0,0,0,0,2,4,4},
    {2,0,5,5,3,0,1,0,0,0,0,0,0,0,0,0,0,5,5},
    {0,0,0,5,0,1,0,2,0,0,0,0,0,0,0,0,3,4,5},
    {0,0,0,5,3,2,3,0,2,0,0,0,0,0,0,0,3,5,4},
    {2,0,6,6,3,2,6,0,3,0,0,0,0,0,0,0,3,6,4},
    {1,0,5,6,6,2,3,0,0,0,0,0,0,0,0,0,0,0,4},
    {0,0,0,5,3,3,5,2,0,0,0,0,0,0,0,0,2,3,4},
    {6,0,6,5,5,2,0,1,0,0,0,0,0,0,0,0,5,4,4},
    {0,0,5,5,4,2,0,1,0,0,0,0,0,0,0,0,0,4,4},
    {1,0,6,5,4,3,2,0,0,0,0,0,0,0,0,0,0,0,6},
    {5,0,0,5,0,2,0,0,1,0,0,0,0,0,0,0,4,4,4},
    {6,0,5,6,4,2,0,1,0,0,0,0,0,0,0,0,0,4,4},
    {2,0,0,5,3,3,3,0,3,0,0,0,0,0,0,0,3,5,4},
    {0,0,0,4,3,3,0,2,0,0,0,0,0,0,0,0,3,2,4},
    {5,0,5,5,5,2,0,0,1,0,0,0,0,0,0,0,0,4,4},
    {0,0,5,0,6,3,2,0,2,0,0,0,0,0,0,0,2,6,4},
    {2,5,0,5,4,2,0,2,0,0,0,0,0,0,0,0,5,5,4},
    {0,0,0,4,4,2,0,1,0,0,0,0,0,0,0,0,0,4,4},
    {6,0,6,5,5,1,0,0,2,0,0,0,0,0,0,0,4,4,5},
    {1,0,5,5,0,2,3,0,0,0,0,0,0,0,0,0,0,0,4},
    {1,0,0,5,5,3,0,2,0,0,0,0,0,0,0,0,5,0,5},
    {0,0,0,5,5,2,0,1,0,0,0,0,0,0,0,0,4,4,4},
    {2,0,0,6,6,2,3,0,3,0,0,0,0,0,0,0,3,4,5},
    {6,0,6,5,5,2,0,0,1,0,0,0,0,0,0,0,0,3,5},
    {2,0,5,5,3,6,1,0,0,0,0,0,0,0,0,0,0,6,5},
    {0,0,0,4,3,2,0,0,2,0,0,0,0,0,0,0,3,4,3},
};

struct GAState {
    DynamicHuffmanBlock block;
    std::vector<Variable> variables;

    GAState(const DynamicHuffmanBlock& b, const std::vector<Variable>& vars) : block(b), variables(vars) {}

    std::vector<int>& cl_code_lengths() {
        return block.cl_code_lengths;
    }
    const std::vector<int>& cl_code_lengths() const {
        return block.cl_code_lengths;
    }
    std::string var_assignments() const {
        std::string s;
        for (int i = 0; i < variables.size(); ++i) {
            if (variables[i].name.size() != 1) continue;
            s += variables[i].name;
        }
        return s;
    }
    int bit_length() const {
        return block.bit_length_with_added_size(); // escape込みで評価
    }
    void print_cl_code_lengths() const {
        for (int i = 0; i < block.cl_code_lengths.size(); ++i) {
            std::cerr << block.cl_code_lengths[i] << (i + 1 == block.cl_code_lengths.size() ? "\n" : " ");
        }
    }
    void print_var_assignment() const {
        std::cerr << var_assignments() << std::endl;
    }
    bool operator<(const GAState& other) const {
        return bit_length() < other.bit_length();
    }
    // hash by cl_code_lengths and var_assignments
    std::size_t hash() const {
        std::size_t seed = 0;
        auto cl_code_lengths_arr = cl_code_lengths();
        auto var_assignments_str = var_assignments();
        for (const auto& val : cl_code_lengths_arr) {
            seed ^= std::hash<int>()(val) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        for (const auto& ch : var_assignments_str) {
            seed ^= std::hash<char>()(ch) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
    void write_to_stream(std::ostream& out) const {
        block.dump_string(out);
        write_variables_to_stream(out, variables);
    }
    static GAState load_from_streram(std::istream& in) {
        auto block = load_block_from_stream(in);
        auto* db = dynamic_cast<DynamicHuffmanBlock*>(block.get());
        if (!db) {
            throw std::runtime_error("Only DynamicHuffmanBlock is supported in GAState");
        }
        auto variables = load_variables_from_stream(in);
        return GAState(*db, variables);
    }
};

std::vector<GAState> load_states(std::string in_filepath) {
    if (in_filepath.empty()) {
        return {};
    }
    std::ifstream in(in_filepath);
    if (!in.is_open()) {
        return {};
    }
    int n;
    in >> n;
    std::vector<GAState> states;
    for (int i = 0; i < n; ++i) {
        states.emplace_back(GAState::load_from_streram(in));
    }
    std::cerr << "Loaded " << states.size() << " states from " << in_filepath << std::endl;
    return states;
}

void write_states(std::string out_filepath, const std::vector<GAState>& states) {
    if (out_filepath.empty()) {
        return;
    }
    std::ofstream out(out_filepath);
    if (!out.is_open()) {
        return;
    }
    out << states.size() << "\n";
    for (const auto& state : states) {
        state.write_to_stream(out);
    }
    std::cerr << "Written " << states.size() << " states to " << out_filepath << std::endl;
}

int main(int argc, char** argv) {
    int num_iter = 10;
    if (argc != 4 && argc != 5 && argc != 6) {
        std::cerr << "Usage: " << argv[0] << " <deflate_dump_file> <variable_dump_file> <output_deflate_dump_file> [output_variable_dump_file] [state_file]\n";
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

    std::string out_deflate_filepath = argv[3];
    std::string out_var_filepath = argc >= 5 ? argv[4] : "";
    std::string state_filepath = argc >= 6 ? argv[5] : "";

    std::cerr << "Deflate text file will be written to: " << out_deflate_filepath << "\n";
    if (argc >= 5) {
        std::cerr << "Variable text file will be written to: " << out_var_filepath << "\n";
    }
    if (argc >= 6) {
        std::cerr << "State text file will be written to: " << state_filepath << "\n";
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
    std::vector<int> swappable_var_indices;
    std::cerr << "Variables:\n";
    for (int i = 0; i < variables.size(); ++i) {
        if (variables[i].name.size() == 1) {
            swappable_var_indices.push_back(i);
        }
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

    auto* db = dynamic_cast<DynamicHuffmanBlock*>(blocks[0].get());
    if (!db) {
        std::cerr << "Warning: variable optimization is only supported for dynamic Huffman blocks. Skipping variable optimization.\n";
        for(const auto& block : blocks) {
            block->dump_string(std::cout);
        }
        return 0;
    }



    auto best_state = GAState(*db, variables);

    [&]() {
        if (out_deflate_filepath.empty() || out_var_filepath.empty()) {
            return;
        }
        std::ifstream deflate_in(out_deflate_filepath);
        std::ifstream var_in(out_var_filepath);
        if (!deflate_in.is_open() || !var_in.is_open()) {
            return;
        }
        try {
            auto block = load_block_from_stream(deflate_in);
            auto* db = dynamic_cast<DynamicHuffmanBlock*>(block.get());
            if (!db) {
                return;
            }
            auto variables = load_variables_from_stream(var_in);
            best_state = GAState(*db, variables);
            std::cerr << "Loaded best state from output files. Bit length: " << best_state.bit_length() << "\n";
        } catch (...) {
            return;
        }
    }();

    auto new_state_hook = [&](const GAState& state) {
        int state_bit_length = state.bit_length();
        int best_bit_length = best_state.bit_length();
        if (state_bit_length <= best_bit_length) {
            best_state = state;
            std::cerr << "New best state found! Bit length: " << best_state.bit_length() << "\n";
            std::cerr << "CL code lengths: ";
            best_state.print_cl_code_lengths();
            std::cerr << "Variable assignment: ";
            best_state.print_var_assignment();
            std::cerr << "Binary byte size: " << best_state.block.encode_to_bytes().first.size() << " bytes\n";
            if (state_bit_length < best_bit_length) {
                std::cerr << "Writing output files...\n";
                std::ofstream out_deflate_file(out_deflate_filepath);
                if (!out_deflate_file.is_open()) {
                    std::cerr << "Error opening output deflate file: " << out_deflate_filepath << "\n";
                    return;
                }
                best_state.block.dump_string(out_deflate_file);
                out_deflate_file.close();

                if (!out_var_filepath.empty()) {
                    std::ofstream out_var_file(out_var_filepath);
                    if (!out_var_file.is_open()) {
                        std::cerr << "Error opening output variable file: " << out_var_filepath << "\n";
                        return;
                    }
                    write_variables_to_stream(out_var_file, best_state.variables, var_dependency);
                    out_var_file.close();
                }
            }
        }
    };


    auto ranking_selection = [&](std::vector<GAState>& population, int num_select) {
        std::sort(population.begin(), population.end());
        std::unordered_set<std::size_t> seen_hashes;
        std::vector<GAState> unique_population; // cl-code-lengths, var-assignmentsでユニークにして多様性確保
        for (const auto& individual : population) {
            auto h = individual.hash();
            if (seen_hashes.count(h) == 0) {
                seen_hashes.insert(h);
                unique_population.push_back(individual);
            }
        }
        population = std::move(unique_population);

        int n = population.size();
        if (num_select > n) num_select = n;
        std::unordered_set<int> selected_indices;
        selected_indices.reserve(num_select * 2);
        std::vector<GAState> new_population;
        new_population.reserve(num_select);
        int total_rank = n * (n + 1) / 2;
        while (selected_indices.size() < static_cast<size_t>(num_select)) {
            int r = XorShift::randn(total_rank);
            int threshold = total_rank;
            int chosen = -1;
            for (int i = 0; i < n; ++i) {
                threshold -= (n - i);
                if (r >= threshold) {
                    chosen = i;
                    break;
                }
            }
            if (selected_indices.count(chosen)) continue;
            selected_indices.insert(chosen);
            new_population.push_back(population[chosen]);
        }
        std::sort(new_population.begin(), new_population.end());
        return new_population;
    };
    
    auto trial = [&](const GAState& state) -> std::pair<GAState, bool> {
        try {
            auto freq_count = XorShift::randn(2) ? FreqCount::NumNonVarAsLiteral : FreqCount::NumNonVarAll;
            auto tie_break = []() {
                int r = XorShift::randn(6);
                if (r == 0) return TieBreak::BFS;
                if (r == 1) return TieBreak::NonVarFreq;
                if (r == 2) return TieBreak::NoUpdate;
                if (r == 3) return TieBreak::RandomSwap;
                if (r == 4) return TieBreak::ChangeVarSet;
                return TieBreak::RandomSwapCL;
            }();
            auto no_update_optimal_parse = XorShift::randn(2) != 0;
            bool finally_update_optimal_parse = XorShift::randn(2) != 0;
            auto var_assign = XorShift::randn(2) ? VariableAssignment::Injective : VariableAssignment::Greedy;
            auto update_cl_code = XorShift::randn(2) != 0;
            auto iterative = XorShift::rand_double() < 0.2;
            auto block = state.block;
            auto variables = state.variables;

            if (tie_break == TieBreak::BFS || tie_break == TieBreak::NonVarFreq) {
                auto variable_to_new_literal_mapping = optimize_variables(block, variables, var_dependency, freq_count, tie_break, var_assign);
                replace_and_recompute_parsing(block, variables, variable_to_new_literal_mapping);
            }
            else if (tie_break == TieBreak::RandomSwap) {

                while (true) {
                    int swapsize = XorShift::randn(std::min(4, (int)swappable_var_indices.size() - 2)) + 2;
                    auto indices = swappable_var_indices;
                    XorShift::shuffle(indices);
                    indices.resize(swapsize);
                    std::vector<int> old_indices = indices;
                    XorShift::shuffle(indices);
                    std::vector<int> var_to_char(variables.size(), -1);
                    for (int i = 0; i < variables.size(); ++i) {
                        int character = static_cast<int>(variables[i].name[0]);
                        var_to_char[i] = character;
                    }
                    std::vector<int> var_to_char_old = var_to_char;
                    for (int i = 0; i < swapsize; ++i) {
                        int var_idx = old_indices[i];
                        int new_char = var_to_char_old[indices[i]];
                        var_to_char[var_idx] = new_char;
                    }
                    std::vector<std::vector<int>> char_to_vars(256);
                    for (int i = 0; i < variables.size(); ++i) {
                        char_to_vars[var_to_char[i]].push_back(i);
                    }
                    bool valid = true;
                    for (int i = 0; i < 256; ++i) {
                        for (int j = 0; j < char_to_vars[i].size(); ++j) {
                            for (int k = j + 1; k < char_to_vars[i].size(); ++k) {
                                if (var_dependency[char_to_vars[i][j]][char_to_vars[i][k]]) {
                                    valid = false;
                                }
                            }
                        }
                    }
                    if (!valid) {
                        continue;
                    }
                    std::vector<int> variable_to_new_literal_mapping(variables.size(), -1);
                    for (int i = 0; i < swapsize; ++i) {
                        int var_idx = old_indices[i];
                        variable_to_new_literal_mapping[var_idx] = var_to_char[var_idx];
                    }
                    replace_and_recompute_parsing(block, variables, variable_to_new_literal_mapping);
                    break;
                }
            }
            else if (tie_break == TieBreak::RandomSwapCL) {
                randomly_update_code_lengths(block.cl_code_lengths);
            }
            else if (tie_break == TieBreak::ChangeVarSet) {
                auto variable_to_new_literal_mapping = optimize_variables(block, variables, var_dependency, freq_count, tie_break, var_assign);
                replace_and_recompute_parsing(block, variables, variable_to_new_literal_mapping);
            }
            else if (no_update_optimal_parse) {
                block.tokens = optimal_parse_block(block, {});
            }
            if (iterative) {
                optimize_huffman_tree(block, {}, false, num_iter);
            }
            else {
                optimize_lit_code_huffman(block);
                optimize_dist_code_huffman(block);
            }

            if (update_cl_code) {
                block.cl_code_lengths = get_optimal_cl_code_lengths(block.literal_code_lengths, block.distance_code_lengths);
                if (iterative) {
                    optimize_huffman_tree(block, {}, false, num_iter);
                }
                else {
                    optimize_lit_code_huffman(block);
                    optimize_dist_code_huffman(block);
                }
            }
            if (finally_update_optimal_parse) {
                block.tokens = optimal_parse_block(block, {});
            }
            return std::make_pair(GAState(block, variables), true);
        }
        catch (const LitCodeDPFailure& e) {
            return std::make_pair(state, false);
        }
        catch (const DistCodeDPFailure& e) {
            return std::make_pair(state, false);
        }
        catch (const RLEDPTable::RLEDPFailure& e) {
            return std::make_pair(state, false);
        }
    };

    auto cross_over = [&](GAState parent1, GAState parent2) -> std::pair<GAState, bool> {
        if (XorShift::randn(2) == 0) {
            std::swap(parent1, parent2);
        }
        bool update_optimal_parse = XorShift::randn(2) != 0;
        bool finally_update_optimal_parse = XorShift::randn(2) != 0;
        auto block = parent1.block;
        auto variables = parent1.variables;
        auto update_cl_code = XorShift::randn(2) != 0;
        auto iterative = XorShift::rand_double() < 0.2;

        auto use_cl_from_parent2 = XorShift::randn(2) == 0;
        try {
            if (use_cl_from_parent2) {
                block.cl_code_lengths = parent2.block.cl_code_lengths;
                optimize_lit_code_huffman(block);
                optimize_dist_code_huffman(block);
            }
            if (update_optimal_parse) {
                block.tokens = optimal_parse_block(block, {});
                optimize_lit_code_huffman(block);
                optimize_dist_code_huffman(block);
            }
            if (iterative) {
                optimize_huffman_tree(block, {}, false, num_iter);
            }
            if (update_cl_code) {
                block.cl_code_lengths = get_optimal_cl_code_lengths(block.literal_code_lengths, block.distance_code_lengths);
                if (iterative) {
                    optimize_huffman_tree(block, {}, false, num_iter);
                }
                else {
                    optimize_lit_code_huffman(block);
                    optimize_dist_code_huffman(block);
                }
            }
            if (finally_update_optimal_parse) {
                block.tokens = optimal_parse_block(block, {});
            }
            block.bit_length(); // sanity check
        }
        catch (const LitCodeDPFailure& e) {
            return std::make_pair(parent1, false);
        }
        catch (const DistCodeDPFailure& e) {
            return std::make_pair(parent1, false);
        }
        catch (const RLEDPTable::RLEDPFailure& e) {
            return std::make_pair(parent1, false);
        }
        return std::make_pair(GAState(block, variables), true);
    };

    // 初期状態を適当に構築
    GAState initial_state(*db, variables);
    std::vector<GAState> states = load_states(state_filepath);

    if (states.size() > 0) {
        std::cerr << "Initial population size (loaded): " << states.size() << "\n";
        for (const auto& state : states) {
            new_state_hook(state);
        }
    }
    else {
        auto init_state_cls = INITIAL_CL_CODE_LENGTHS;
        init_state_cls.push_back(db->cl_code_lengths);
        std::cerr << "Initial CL code lengths candidates: " << init_state_cls.size() << "\n";
        for (auto& cl : init_state_cls) {
            auto block = initial_state.block;
            auto variables = initial_state.variables;
            block.cl_code_lengths = cl;
            try {
                optimize_lit_code_huffman(block); // cl codeを弄ったらtrial前にこれを挟まないとinvalidな状態が生まれて死ぬ
                optimize_dist_code_huffman(block);
            }
            catch (const LitCodeDPFailure& e) {
                continue;
            }
            catch (const DistCodeDPFailure& e) {
                continue;
            }
            try {
                auto [s, b] = trial(GAState(block, variables));
                if (!b) continue;
                new_state_hook(s);
                states.emplace_back(s);
            }
            catch (const RLEDPTable::RLEDPFailure& e) {
                continue;
            }
        }
    }

    constexpr int POPULATION_SIZE = 100;
    constexpr int CROSSOVER_SIZE = 100;

    states = ranking_selection(states, POPULATION_SIZE);

    while (true) {
        for (const auto& state : states) {
            std::cerr << "State bit length: " << state.bit_length() << "\n";
            std::cerr << "  ";
            state.print_cl_code_lengths();
            std::cerr << "  ";
            state.print_var_assignment();
        }

        std::vector<GAState> new_states;
        std::cerr << "Cross over size: " << CROSSOVER_SIZE << "\n";
        for (int i = 0; i < CROSSOVER_SIZE; ++i) {
            int idx1 = XorShift::randn(states.size());
            int idx2 = XorShift::randn(states.size());
            while (idx2 == idx1) {
                idx2 = XorShift::randn(states.size());
            }
            auto [s, b] = cross_over(states[idx1], states[idx2]);
            if (!b) continue;
            new_state_hook(s);
            new_states.push_back(s);
        }
        std::cerr << "Mutation size: " << states.size() << "\n";
        for (const auto& state : states) {
            new_states.push_back(state);
            auto [s, b] = trial(state);
            if (!b) continue;
            new_state_hook(s);
            new_states.push_back(s);
        }
        if (new_states.size() == 0) {
            std::cerr << "No new states generated. Stopping.\n";
            break;
        }
        states = ranking_selection(new_states, POPULATION_SIZE);
        write_states(state_filepath, states);
        std::cerr << "Population size: " << states.size() << ", Best length so far: " << best_state.bit_length() << "\n";
    }

    auto best_block = best_state.block;

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

    return 0;
}
