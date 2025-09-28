#pragma once
#include <string>
#include <fstream>
#include <vector>

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