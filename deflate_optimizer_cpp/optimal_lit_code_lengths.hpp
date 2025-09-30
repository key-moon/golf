#pragma once
#include "blocks.hpp"

class LitCodeDPFailure : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;
};

class DistCodeDPFailure : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;
};

void optimize_lit_code_huffman_slow(DynamicHuffmanBlock& block, int MAX_BIT_WIDTH=9) {
    std::vector<int> lit_freq(286, 0);
    std::vector<int> dist_freq(30, 0);
    for (const auto& token : block.tokens) {
        if (token.type == Token::LITERAL) {
            lit_freq[token.literal]++;
        } else {
            int len_code = convert_length_value_to_code(token.pair.length);
            int dist_code = convert_distance_value_to_code(token.pair.distance);
            lit_freq[len_code]++;
            dist_freq[dist_code]++;
        }
    }
    lit_freq[256] = 1;
    while(lit_freq.size() > 257 && lit_freq.back() == 0) lit_freq.pop_back();
    while(dist_freq.size() > 1 && dist_freq.back() == 0) dist_freq.pop_back();

    std::vector<std::vector<std::vector<int>>> dp(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, 1e6)));
    std::vector<std::vector<std::vector<int>>> last_run_code(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, -1)));
    std::vector<std::vector<std::vector<int>>> last_run_length(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, -1)));

    std::vector<int> RLE_symbols_cost = block.cl_code_lengths;
    for(auto& l : RLE_symbols_cost) {
        if (l == 0) l = 1e6;
    }

    auto compute_run_cost = [&RLE_symbols_cost](int prev_code, int last_run_code, int last_run_length) {
        if (last_run_length == 1) {
            return RLE_symbols_cost[last_run_code];
        }
        else if(prev_code == last_run_code) {
            if (3 <= last_run_length && last_run_length <= 6) {
                return RLE_symbols_cost[16] + 2;
            }
        } else if (last_run_code == 0) {
            if (3 <= last_run_length && last_run_length <= 10) {
                return RLE_symbols_cost[17] + 3;
            }
            else if (11 <= last_run_length && last_run_length <= 138) {
                return RLE_symbols_cost[18] + 7;
            }
        }
        return (int)1e6;
    };
    
    dp[0][0][1] = 0;

    for (int i = 0; i < lit_freq.size(); ++i) {
        for (int j = 0; j <= (1 << MAX_BIT_WIDTH); ++j) {
            for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
                if (dp[i][j][prev_code] == 1e6) continue;
                for (int code = 0; code <= MAX_BIT_WIDTH; ++code) {
                    int maximum_length = code == 0 ? 138 : 6;
                    int next_j = j;
                    int lit_cost = 0;
                    for (int run_length = 1; run_length <= maximum_length; ++run_length) {
                        if (i + run_length >= dp.size()) break;
                        next_j += (code == 0 ? 0 : (1 << (MAX_BIT_WIDTH - code)));
                        lit_cost += lit_freq[i + run_length - 1] * code;
                        if (lit_freq[i + run_length - 1] != 0 && code == 0) break;
                        if (next_j > (1 << MAX_BIT_WIDTH)) break;
                        int run_cost = compute_run_cost(prev_code, code, run_length);
                        int cost = dp[i][j][prev_code] + run_cost + lit_cost;
                        if (dp[i + run_length][next_j][code] > cost) {
                            dp[i + run_length][next_j][code] = cost;
                            last_run_code[i + run_length][next_j][code] = prev_code;
                            last_run_length[i + run_length][next_j][code] = run_length;
                        }
                    }
                }
            }
        }
    }

    const auto& dp_back = dp[lit_freq.size()][(1 << MAX_BIT_WIDTH)];
    std::pair<int,int> best = {1e6, 1e6};
    for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
        int cost = dp_back[prev_code];
        auto p = std::make_pair(cost, prev_code);
        if (p < best) {
            best = p;
        }
    }

    int best_cost = best.first;
    int code = best.second;
    std::vector<int> new_lit_code_lengths(lit_freq.size(), 0);
    int i = lit_freq.size();
    int j = (1 << MAX_BIT_WIDTH);
    while(i > 0) {
        int prev_code = last_run_code[i][j][code];
        int run_length = last_run_length[i][j][code];
        for (int k = 0; k < run_length; ++k) {
            new_lit_code_lengths[--i] = code;
            j -= (code == 0 ? 0 : (1 << (MAX_BIT_WIDTH - code)));
        }
        code = prev_code;
    }
    block.literal_code_lengths = new_lit_code_lengths;
 }

void optimize_lit_code_huffman_fast(DynamicHuffmanBlock& block, int MAX_BIT_WIDTH=9) {

    std::vector<int> lit_freq(286, 0);
    std::vector<int> dist_freq(30, 0);
    for (const auto& token : block.tokens) {
        if (token.type == Token::LITERAL) {
            lit_freq[token.literal]++;
        } else {
            int len_code = convert_length_value_to_code(token.pair.length);
            int dist_code = convert_distance_value_to_code(token.pair.distance);
            lit_freq[len_code]++;
            dist_freq[dist_code]++;
        }
    }
    lit_freq[256] = 1;
    while(lit_freq.size() > 257 && lit_freq.back() == 0) lit_freq.pop_back();
    while(dist_freq.size() > 1 && dist_freq.back() == 0) dist_freq.pop_back();

    int score_ub = [&](){
        auto tmp_literal_code_lengths = block.literal_code_lengths;
        auto tmp_distance_code_lengths = block.distance_code_lengths;
        if (tmp_literal_code_lengths.empty()) {
            // set fixed code
            tmp_literal_code_lengths.resize(286);
            for (int i = 0; i <= 143; ++i) tmp_literal_code_lengths[i] = 8;
            for (int i = 144; i <= 255; ++i) tmp_literal_code_lengths[i] = 9;
            for (int i = 256; i <= 279; ++i) tmp_literal_code_lengths[i] = 7;
            for (int i = 280; i <= 285; ++i) tmp_literal_code_lengths[i] = 8;
        }
        if (tmp_distance_code_lengths.empty()) {
            tmp_distance_code_lengths.resize(30, 5);
        }
        auto compute = [&](){

            std::vector<RLECode> rle_codes;
            try {
                rle_codes = compute_RLE_encoded_representation(tmp_literal_code_lengths, tmp_distance_code_lengths, block.cl_code_lengths);
            } catch (...) {
                return (int)1e6 - 1;
            }
            int score = 0;
            for (const auto& code : rle_codes) {
                score += block.cl_code_lengths[code.id()];
                score += code.num_additional_bits();
            }
            for (auto tok : block.tokens) {
                if (tok.type == Token::LITERAL) {
                    score += tmp_literal_code_lengths[tok.literal];
                } else { // COPY
                    int lit_code = convert_length_value_to_code(tok.pair.length);
                    int distance_code = convert_distance_value_to_code(tok.pair.distance);
                    score += tmp_literal_code_lengths[lit_code];
                    score += num_additional_bits_for_len(tok.pair.length);
                    score += tmp_distance_code_lengths[distance_code];
                    score += num_additional_bits_for_dist(tok.pair.distance);
                }
            }
            return score;
        };
        int sc1 = compute();
        tmp_literal_code_lengths = compute_huff_code_lengths_from_frequencies(lit_freq);
        tmp_distance_code_lengths = compute_huff_code_lengths_from_frequencies(dist_freq);
        int sc2 = compute();
        return std::min(sc1, sc2);
    }();

    std::vector<std::vector<std::vector<int>>> dp(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, 1e6)));
    std::vector<std::vector<std::vector<int>>> last_run_code(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, -1)));
    std::vector<std::vector<std::vector<int>>> last_run_length(lit_freq.size() + 1, std::vector<std::vector<int>>((1 << MAX_BIT_WIDTH) + 1, std::vector<int>(MAX_BIT_WIDTH + 1, -1)));

    std::vector<int> RLE_symbols_cost = block.cl_code_lengths;
    for(auto& l : RLE_symbols_cost) {
        if (l == 0) l = 1e6;
    }

    dp[0][0][0] = 0;

    struct QueState {
        int cost;
        int prev_code;
        int i;
    };

    std::vector<int> lit_freq_cumsum(lit_freq.size() + 1, 0);
    for (int i = 0; i < lit_freq.size(); ++i) {
        lit_freq_cumsum[i + 1] = lit_freq_cumsum[i] + lit_freq[i];
    }

    std::vector<std::deque<QueState>> min_que_17((1 << MAX_BIT_WIDTH) + 1);
    std::vector<std::deque<QueState>> min_que_18((1 << MAX_BIT_WIDTH) + 1);

    for (int i = 0; i <= lit_freq.size(); ++i) {
        for (int j = 0; j <= (1 << MAX_BIT_WIDTH); ++j) {

            // 0を選ぶ場合: もらうDPで累積minを取って高速化
            // dp[i][j][0] = min_{1 <= len <= 138} (dp[i-len][j][0] + cost_of_run(0, 0, len))
            // 3 <= len <= 10, 11 <= len <= 138 の場合に分ける
            // これはスライド最小値で実現できる
            if (i && lit_freq[i - 1] != 0) { // 直前の文字の出現頻度が非0ならqueueをリセット
                min_que_17[j].clear();
                min_que_18[j].clear();
            }
            else {
                if (i >= 3 && lit_freq_cumsum[i] == lit_freq_cumsum[i - 3]) { // 直近3文字が全部ゼロ
                    int min_cost = 1e6;
                    int cost_min_prev_code = 1e6;
                    for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
                        if (dp[i - 3][j][prev_code] < min_cost) {
                            min_cost = dp[i - 3][j][prev_code];
                            cost_min_prev_code = prev_code;
                        }
                    }
                    int cost_17 = min_cost + RLE_symbols_cost[17] + 3;
                    QueState state_17 = {cost_17, cost_min_prev_code, i - 3};
                    while (!min_que_17[j].empty() && min_que_17[j].back().cost >= state_17.cost) {
                        min_que_17[j].pop_back();
                    }
                    min_que_17[j].push_back(state_17);
                    while (!min_que_17[j].empty() && i - min_que_17[j].front().i > 10) {
                        min_que_17[j].pop_front();
                    }
                    int cost = min_que_17[j].front().cost;
                    int prev_code = min_que_17[j].front().prev_code;
                    if (dp[i][j][0] > cost) {
                        dp[i][j][0] = cost;
                        last_run_code[i][j][0] = prev_code;
                        last_run_length[i][j][0] = i - min_que_17[j].front().i;
                    }
                }
                if (i >= 11 && lit_freq_cumsum[i] == lit_freq_cumsum[i - 11]) {
                    int min_cost = 1e6;
                    int cost_min_prev_code = 1e6;
                    for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
                        if (dp[i - 11][j][prev_code] < min_cost) {
                            min_cost = dp[i - 11][j][prev_code];
                            cost_min_prev_code = prev_code;
                        }
                    }
                    int cost_18 = min_cost + RLE_symbols_cost[18] + 7;
                    QueState state_18 = {cost_18, cost_min_prev_code, i - 11};
                    while (!min_que_18[j].empty() && min_que_18[j].back().cost >= state_18.cost) {
                        min_que_18[j].pop_back();
                    }
                    min_que_18[j].push_back(state_18);
                    while (!min_que_18[j].empty() && i - min_que_18[j].front().i > 138) {
                        min_que_18[j].pop_front();
                    }
                    int cost = min_que_18[j].front().cost;
                    int prev_code = min_que_18[j].front().prev_code;
                    if (dp[i][j][0] > cost) {
                        dp[i][j][0] = cost;
                        last_run_code[i][j][0] = prev_code;
                        last_run_length[i][j][0] = i - min_que_18[j].front().i;
                    }
                }
            }

            if (i == lit_freq.size()) continue;

            int min_cost = 1e6;
            int cost_min_prev_code = 1e6;
            for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
                if (dp[i][j][prev_code] < min_cost) {
                    min_cost = dp[i][j][prev_code];
                    cost_min_prev_code = prev_code;
                }
            }

            if (min_cost > score_ub) continue;

            // 単一コードを使う場合: prev_codeに遷移が関係ないので先にminを取っていい
            for (int code = 0; code <= MAX_BIT_WIDTH; ++code) {
                int next_j = j + (code == 0 ? 0 : (1 << (MAX_BIT_WIDTH - code)));
                if (next_j > (1 << MAX_BIT_WIDTH)) continue;
                if (lit_freq[i] != 0 && code == 0) continue;
                int cost = min_cost + RLE_symbols_cost[code] + lit_freq[i] * code;
                if (dp[i + 1][next_j][code] > cost) {
                    dp[i + 1][next_j][code] = cost;
                    last_run_code[i + 1][next_j][code] = cost_min_prev_code;
                    last_run_length[i + 1][next_j][code] = 1;
                }
            }

            // code 16 の場合: 3 <= len <= 6 で配るDP
            int run_cost_16 = RLE_symbols_cost[16] + 2;
            for (int code = 0; code <= MAX_BIT_WIDTH; ++code) {
                if (i == 0) continue; // DPの初期化の都合でこれを弾く必要がある
                if (dp[i][j][code] > score_ub) continue;
                for (int run_length = 3; run_length <= 6; ++run_length) {
                    if (i + run_length > lit_freq.size()) break;
                    int next_j = j + (code == 0 ? 0 : (1 << (MAX_BIT_WIDTH - code))) * run_length;
                    if (next_j > (1 << MAX_BIT_WIDTH)) break;
                    int sum_lit_freq = lit_freq_cumsum[i + run_length] - lit_freq_cumsum[i];
                    if (sum_lit_freq != 0 && code == 0) break;
                    int lit_cost = sum_lit_freq * code;
                    int cost = dp[i][j][code] + run_cost_16 + lit_cost;
                    if (cost > score_ub) break;
                    if (dp[i + run_length][next_j][code] > cost) {
                        dp[i + run_length][next_j][code] = cost;
                        last_run_code[i + run_length][next_j][code] = code;
                        last_run_length[i + run_length][next_j][code] = run_length;
                    }
                }
            }
        }
    }

    const auto& dp_back = dp[lit_freq.size()][(1 << MAX_BIT_WIDTH)];
    std::pair<int,int> best = {1e6, 1e6};
    for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
        int cost = dp_back[prev_code];
        auto p = std::make_pair(cost, prev_code);
        if (p < best) {
            best = p;
        }
    }

    int best_cost = best.first;
    if (best_cost == 1e6) {
        throw LitCodeDPFailure("Literal code DP failed: ans = INF");
    }
    int code = best.second;
    std::vector<int> new_lit_code_lengths(lit_freq.size(), 0);
    int i = lit_freq.size();
    int j = (1 << MAX_BIT_WIDTH);

    while(i > 0) {
        int prev_code = last_run_code[i][j][code];
        int run_length = last_run_length[i][j][code];
        for (int k = 0; k < run_length; ++k) {
            new_lit_code_lengths[--i] = code;
            j -= (code == 0 ? 0 : (1 << (MAX_BIT_WIDTH - code)));
        }
        code = prev_code;
    }
    block.literal_code_lengths = new_lit_code_lengths;
 }

void optimize_dist_code_huffman(DynamicHuffmanBlock& block, int MAX_BIT_WIDTH=6) {
    std::vector<int> dist_freq(30, 0);
    for (const auto& token : block.tokens) {
        if (token.type == Token::COPY) {
            int dist_code = convert_distance_value_to_code(token.pair.distance);
            dist_freq[dist_code]++;
        }
    }
    while(dist_freq.size() > 1 && dist_freq.back() == 0) dist_freq.pop_back();

    if (dist_freq.empty()) {
        block.distance_code_lengths.clear();
        return;
    }

    constexpr int INF = 1e6;
    const int SYMBOL_COUNT = static_cast<int>(dist_freq.size());
    const int MAX_OCCUPANCY = (1 << MAX_BIT_WIDTH);

    std::vector<std::vector<std::vector<int>>> dp(
        SYMBOL_COUNT + 1,
        std::vector<std::vector<int>>(MAX_OCCUPANCY + 1, std::vector<int>(MAX_BIT_WIDTH + 1, INF))
    );
    std::vector<std::vector<std::vector<int>>> last_run_code(
        SYMBOL_COUNT + 1,
        std::vector<std::vector<int>>(MAX_OCCUPANCY + 1, std::vector<int>(MAX_BIT_WIDTH + 1, -1))
    );
    std::vector<std::vector<std::vector<int>>> last_run_length(
        SYMBOL_COUNT + 1,
        std::vector<std::vector<int>>(MAX_OCCUPANCY + 1, std::vector<int>(MAX_BIT_WIDTH + 1, -1))
    );

    std::vector<int> RLE_symbols_cost = block.cl_code_lengths;
    if (RLE_symbols_cost.size() < 19) {
        RLE_symbols_cost.resize(19, INF);
    }
    for (auto& l : RLE_symbols_cost) {
        if (l == 0) l = INF;
    }

    auto compute_run_cost = [&RLE_symbols_cost](int prev_code, int run_code, int run_length) {
        if (run_length == 1) {
            return RLE_symbols_cost[run_code];
        }
        if (prev_code == run_code) {
            if (3 <= run_length && run_length <= 6) {
                return RLE_symbols_cost[16] + 2;
            }
        } else if (run_code == 0) {
            if (3 <= run_length && run_length <= 10) {
                return RLE_symbols_cost[17] + 3;
            }
            if (11 <= run_length && run_length <= 138) {
                return RLE_symbols_cost[18] + 7;
            }
        }
        return INF;
    };

    dp[0][0][1] = 0;

    for (int i = 0; i < SYMBOL_COUNT; ++i) {
        for (int j = 0; j <= MAX_OCCUPANCY; ++j) {
            for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
                if (dp[i][j][prev_code] >= INF) continue;
                for (int code = 0; code <= MAX_BIT_WIDTH; ++code) {
                    int maximum_length = code == 0 ? 138 : 6;
                    int next_j = j;
                    int dist_cost = 0;
                    for (int run_length = 1; run_length <= maximum_length; ++run_length) {
                        if (i + run_length > SYMBOL_COUNT) break;
                        if (code != 0) {
                            next_j += (1 << (MAX_BIT_WIDTH - code));
                        }
                        if (next_j > MAX_OCCUPANCY) break;
                        dist_cost += dist_freq[i + run_length - 1] * code;
                        if (dist_freq[i + run_length - 1] != 0 && code == 0) break;
                        int run_cost = compute_run_cost(prev_code, code, run_length);
                        if (run_cost >= INF) continue;
                        int cost = dp[i][j][prev_code] + run_cost + dist_cost;
                        if (cost >= dp[i + run_length][next_j][code]) continue;
                        dp[i + run_length][next_j][code] = cost;
                        last_run_code[i + run_length][next_j][code] = prev_code;
                        last_run_length[i + run_length][next_j][code] = run_length;
                    }
                }
            }
        }
    }

    const auto& dp_back = dp[SYMBOL_COUNT][MAX_OCCUPANCY];
    std::pair<int, int> best = {INF, INF};
    for (int prev_code = 0; prev_code <= MAX_BIT_WIDTH; ++prev_code) {
        int cost = dp_back[prev_code];
        auto candidate = std::make_pair(cost, prev_code);
        if (candidate < best) {
            best = candidate;
        }
    }

    if (best.first >= INF) {
        throw DistCodeDPFailure("Distance code DP failed: ans = INF");
    }

    int code = best.second;
    int i = SYMBOL_COUNT;
    int j = MAX_OCCUPANCY;
    std::vector<int> new_dist_code_lengths(SYMBOL_COUNT, 0);
    while (i > 0) {
        int prev_code = last_run_code[i][j][code];
        int run_length = last_run_length[i][j][code];
        if (run_length <= 0) {
            throw std::runtime_error("Invalid run length in distance code optimization");
        }
        for (int k = 0; k < run_length; ++k) {
            new_dist_code_lengths[--i] = code;
            if (code != 0) {
                j -= (1 << (MAX_BIT_WIDTH - code));
            }
        }
        code = prev_code;
    }
    block.distance_code_lengths = new_dist_code_lengths;
}


void optimize_lit_code_huffman(DynamicHuffmanBlock& block, int MAX_BIT_WIDTH=9) {
    // optimize_lit_code_huffman_slow(block, MAX_BIT_WIDTH);
    // std::cerr << "Optimizing lit code lengths (fast)..." << std::endl;
    optimize_lit_code_huffman_fast(block, MAX_BIT_WIDTH);
    // std::cerr << "Done." << std::endl;
}
