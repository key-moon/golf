#pragma once
#include <string>
#include <fstream>
#include <vector>
#include <unordered_map>

struct Variable {
    std::string name;
    std::vector<int> occurrences;
};

std::vector<Variable> load_variables_from_stream(std::istream& in) {
    int n;
    in >> n;
    std::vector<Variable> vars(n);
    for (int i = 0; i < n; ++i) {
        in >> vars[i].name;
        int m;
        in >> m;
        vars[i].occurrences.resize(m);
        for (int j = 0; j < m; ++j) {
            in >> vars[i].occurrences[j];
        }
    }
    return vars;
}

std::vector<std::vector<bool>> load_dependency_matrix_from_stream(std::istream& in, int num_vars) {
    std::vector<std::vector<bool>> conflict_matrix(num_vars, std::vector<bool>(num_vars, false));
    for (int i = 0; i < num_vars; ++i) {
        for (int j = 0; j < num_vars; ++j) {
            int x;
            in >> x;
            conflict_matrix[i][j] = x;
        }
    }
    return conflict_matrix;
}

void merge_samename_variable(std::vector<Variable>& vars, std::vector<std::vector<bool>>& var_dependency) {
    // 複数のvariableが同じ名前を持つ場合、1つにまとめる
    // dependency行列も更新する (ORをとる)
    if (vars.empty()) {
        var_dependency.clear();
        return;
    }

    std::unordered_map<std::string, std::vector<int>> name_to_indices;
    std::vector<std::string> ordered_names;
    ordered_names.reserve(vars.size());
    for (int i = 0; i < vars.size(); ++i) {
        auto& bucket = name_to_indices[vars[i].name];
        if (bucket.empty()) {
            ordered_names.push_back(vars[i].name);
        }
        bucket.push_back(i);
    }

    if (ordered_names.size() == vars.size()) {
        return;
    }

    std::vector<Variable> merged_vars;
    merged_vars.reserve(ordered_names.size());
    for (const auto& name : ordered_names) {
        Variable merged;
        merged.name = name;
        for (int idx : name_to_indices[name]) {
            const auto& occ = vars[idx].occurrences;
            merged.occurrences.insert(merged.occurrences.end(), occ.begin(), occ.end());
        }
        std::sort(merged.occurrences.begin(), merged.occurrences.end());
        merged_vars.push_back(std::move(merged));
    }

    std::vector<std::vector<bool>> merged_dependency(ordered_names.size(), std::vector<bool>(ordered_names.size(), false));
    for (int i = 0; i < ordered_names.size(); ++i) {
        for (int j = 0; j < ordered_names.size(); ++j) {
            bool dependent = false;
            for (int orig_i : name_to_indices[ordered_names[i]]) {
                for (int orig_j : name_to_indices[ordered_names[j]]) {
                    if (orig_i < var_dependency.size() && orig_j < var_dependency[orig_i].size() && var_dependency[orig_i][orig_j]) {
                        dependent = true;
                        break;
                    }
                }
                if (dependent) break;
            }
            merged_dependency[i][j] = dependent;
        }
    }

    vars = std::move(merged_vars);
    var_dependency = std::move(merged_dependency);
}

void write_variables_to_stream(std::ostream& out, std::vector<Variable> variables, std::vector<std::vector<bool>> var_dependency) {
    merge_samename_variable(variables, var_dependency);
    out << variables.size() << "\n";
    for (const auto& var : variables) {
        out << var.name << " " << var.occurrences.size() << "\n";
        for (int i = 0; i < var.occurrences.size(); ++i) {
            out << var.occurrences[i] << (i + 1 == var.occurrences.size() ? "\n" : " ");
        }
    }
    for (int i = 0; i < variables.size(); ++i) {
        for (int j = 0; j < variables.size(); ++j) {
            out << var_dependency[i][j] << (j + 1 == variables.size() ? "\n" : " ");
        }
    }
}

void write_variables_to_stream(std::ostream& out, std::vector<Variable> variables) {
    out << variables.size() << "\n";
    for (const auto& var : variables) {
        out << var.name << " " << var.occurrences.size() << "\n";
        for (int i = 0; i < var.occurrences.size(); ++i) {
            out << var.occurrences[i] << (i + 1 == var.occurrences.size() ? "\n" : " ");
        }
    }
}