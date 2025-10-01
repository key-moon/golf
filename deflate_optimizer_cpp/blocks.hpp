#pragma once
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <memory>
#include <queue>
#include <unordered_map>
#include <cstdint>
#include <stdexcept>
#include <utility>
#include <array>
#include <limits>

struct BitWriter {
    // Packs individual bits in little-endian order as required by DEFLATE.
    void write_bits(uint32_t bits, int count) {
        if (count <= 0) {
            return;
        }
        uint64_t mask = (count >= 32) ? 0xffffffffull : ((1ull << count) - 1ull);
        bit_buffer_ |= (static_cast<uint64_t>(bits) & mask) << bit_count_;
        bit_count_ += count;
        while (bit_count_ >= 8) {
            bytes_.push_back(static_cast<unsigned char>(bit_buffer_ & 0xffu));
            bit_buffer_ >>= 8;
            bit_count_ -= 8;
        }
    }

    std::vector<unsigned char> take_bytes() {
        if (bit_count_ > 0) {
            bytes_.push_back(static_cast<unsigned char>(bit_buffer_ & 0xffu));
            bit_buffer_ = 0;
            bit_count_ = 0;
        }
        return std::move(bytes_);
    }

    int get_bit_length() const {
        return static_cast<int>(bytes_.size()) * 8 + bit_count_;
    }

private:
    std::vector<unsigned char> bytes_;
    uint64_t bit_buffer_ = 0;
    int bit_count_ = 0;
};

inline std::string repeat_backslash(std::size_t count) {
    return std::string(count, '\\');
}

inline void replace_all(std::string& target, const std::string& from, const std::string& to) {
    if (from.empty()) {
        return;
    }
    std::size_t pos = 0;
    while ((pos = target.find(from, pos)) != std::string::npos) {
        target.replace(pos, from.size(), to);
        pos += to.size();
    }
}

inline uint16_t reverse_bits(uint16_t code, int bit_length) {
    uint16_t res = 0;
    for (int i = 0; i < bit_length; ++i) {
        res = static_cast<uint16_t>((res << 1) | (code & 1u));
        code >>= 1;
    }
    return res;
}

inline std::vector<uint16_t> build_reversed_canonical_codes(const std::vector<int>& code_lengths) {
    int max_len = 0;
    for (int len : code_lengths) {
        if (len > max_len) {
            max_len = len;
        }
    }
    if (max_len == 0) {
        return std::vector<uint16_t>(code_lengths.size(), 0);
    }

    std::vector<int> bl_count(max_len + 1, 0);
    for (int len : code_lengths) {
        if (len > 0) {
            ++bl_count[len];
        }
    }

    std::vector<uint16_t> next_code(max_len + 1, 0);
    uint16_t code = 0;
    for (int bits = 1; bits <= max_len; ++bits) {
        code = static_cast<uint16_t>((code + bl_count[bits - 1]) << 1);
        next_code[bits] = code;
    }

    std::vector<uint16_t> codes(code_lengths.size(), 0);
    for (int symbol = 0; symbol < static_cast<int>(code_lengths.size()); ++symbol) {
        int len = code_lengths[symbol];
        if (len == 0) {
            continue;
        }
        uint16_t canonical = next_code[len]++;
        codes[symbol] = reverse_bits(canonical, len);
    }
    return codes;
}

static const std::string DOUBLE_ESCAPE_PLACEHOLDER = "%DOUBLE_ESCAPE%";

static const std::array<std::string, 21> SHOULD_ESCAPES = {
    std::string("\\\""), std::string("\\'"), std::string("\\0"), std::string("\\1"),
    std::string("\\2"), std::string("\\3"), std::string("\\4"), std::string("\\5"),
    std::string("\\6"), std::string("\\7"), std::string("\\N"), std::string("\\U"),
    std::string("\\a"), std::string("\\b"), std::string("\\f"), std::string("\\n"),
    std::string("\\r"), std::string("\\t"), std::string("\\u"), std::string("\\v"),
    std::string("\\x")
};

inline std::string compute_python_embed_string(const std::string& input) {
    std::string b = input;
    replace_all(b, "\\\\", DOUBLE_ESCAPE_PLACEHOLDER);

    for (const auto& esc : SHOULD_ESCAPES) {
        std::string replacement = "\\" + esc;
        replace_all(b, esc, replacement);
    }

    for (int i = 0; i < 8; ++i) {
        char digit = static_cast<char>('0' + i);
        std::string suffix(1, digit);

        std::string pattern1 = "\\";
        pattern1.push_back('\0');
        pattern1 += suffix;
        std::string replacement1 = repeat_backslash(3) + "000" + suffix;
        replace_all(b, pattern1, replacement1);

        std::string pattern2(1, '\0');
        pattern2 += suffix;
        std::string replacement2 = "\\000" + suffix;
        replace_all(b, pattern2, replacement2);
    }

    std::string pattern_backslash_null = "\\";
    pattern_backslash_null.push_back('\0');
    std::string replacement_backslash_null = repeat_backslash(3) + "0";
    replace_all(b, pattern_backslash_null, replacement_backslash_null);

    std::string pattern_null(1, '\0');
    std::string replacement_null = "\\0";
    replace_all(b, pattern_null, replacement_null);

    std::string pattern_backslash_cr = "\\";
    pattern_backslash_cr.push_back('\r');
    std::string replacement_backslash_cr = repeat_backslash(3) + "r";
    replace_all(b, pattern_backslash_cr, replacement_backslash_cr);

    std::string pattern_cr(1, '\r');
    std::string replacement_cr = "\\r";
    replace_all(b, pattern_cr, replacement_cr);

    if (!b.empty() && b.back() == '\\') {
        b.push_back('\\');
    }

    std::vector<std::string> candidates;
    candidates.reserve(4);

    auto add_single_quote_candidate = [&](char sep_char) {
        std::string t = b;

        std::string pattern_backslash_newline = "\\";
        pattern_backslash_newline.push_back('\n');
        std::string replacement_backslash_newline = repeat_backslash(3) + "n";
        replace_all(t, pattern_backslash_newline, replacement_backslash_newline);

        std::string pattern_newline(1, '\n');
        std::string replacement_newline = "\\n";
        replace_all(t, pattern_newline, replacement_newline);

        std::string sep_str(1, sep_char);
        std::string replacement_sep = "\\";
        replacement_sep.push_back(sep_char);
        replace_all(t, sep_str, replacement_sep);

        replace_all(t, DOUBLE_ESCAPE_PLACEHOLDER, repeat_backslash(4));

        std::string candidate = sep_str + t + sep_str;
        candidates.push_back(std::move(candidate));
    };

    add_single_quote_candidate('\'');
    add_single_quote_candidate('"');

    auto add_triple_quote_candidate = [&](const std::string& sep) {
        if (b.find(sep) != std::string::npos) {
            return;
        }
        std::string t = b;

        std::string pattern_backslash_newline = "\\";
        pattern_backslash_newline.push_back('\n');
        std::string replacement_backslash_newline = repeat_backslash(2);
        replacement_backslash_newline.push_back('\n');
        replace_all(t, pattern_backslash_newline, replacement_backslash_newline);

        replace_all(t, DOUBLE_ESCAPE_PLACEHOLDER, repeat_backslash(4));

        if (!t.empty() && t.back() == sep.front()) {
            t.insert(t.size() - 1, 1, '\\');
        }

        std::string candidate = sep + t + sep;
        candidates.push_back(std::move(candidate));
    };

    add_triple_quote_candidate("'''");
    add_triple_quote_candidate("\"\"\"");

    if (candidates.empty()) {
        return std::string("''");
    }

    return *std::min_element(candidates.begin(), candidates.end(), [](const std::string& lhs, const std::string& rhs) {
        return lhs.size() < rhs.size();
    });
}

inline std::vector<unsigned char> get_embed_string_bytes(const std::vector<unsigned char>& data) {
    std::string input(reinterpret_cast<const char*>(data.data()), data.size());
    std::string escaped = compute_python_embed_string(input);
    return std::vector<unsigned char>(escaped.begin(), escaped.end());
}

inline std::size_t compute_added_bytes_for_embed(const std::vector<unsigned char>& data) {
    auto escaped = get_embed_string_bytes(data);
    if (escaped.size() <= data.size()) {
        return 0;
    }
    return escaped.size() - data.size();
}

struct Block {
    bool bfinal;
    virtual void dump_string(std::ostream& out) const = 0;
    virtual int bit_length() const = 0;
    virtual std::vector<int> get_string(const std::vector<int>& context) const = 0;
};

struct Token {
    enum Type { LITERAL, COPY } type;
    union {
        unsigned char literal;
        struct { int length; int distance; } pair;
    };
    std::string get_string() const {
        if (type == LITERAL) {
            return "L " + std::to_string(static_cast<int>(literal));
        } else {
            return "M " + std::to_string(pair.length) + " " + std::to_string(pair.distance);
        }
    }
    // equal operator
    bool operator==(const Token& other) const {
        if (type != other.type) return false;
        if (type == LITERAL) {
            return literal == other.literal;
        } else {
            return pair.length == other.pair.length && pair.distance == other.pair.distance;
        }
    }
};

struct RLEEntry {
    int value;
    int count;
};

struct RLECode {
    enum Type { LITERAL, PREV_RUN, ZERO_RUN } type;
    int value; // literal value for LITERAL, run length for PREV_RUN and ZERO_RUN
    int num_additional_bits() const {
        if (type == LITERAL) return 0;
        else if (type == PREV_RUN) {
            if (3 <= value && value <= 6) return 2;
            else throw std::runtime_error("Invalid PREV_RUN length");
        } else { // ZERO_RUN
            if (value <= 10) return 3;
            else if (value <= 138) return 7;
            else throw std::runtime_error("Invalid ZERO_RUN length");
        }
    }
    int id() const {
        if(type == LITERAL) {
           return value;
        }
        else if (type == PREV_RUN) {
            return 16;
        }
        else { // ZERO_RUN
            return (value <= 10) ? 17 : 18;
        }
    }
};

struct RLEDPTable {
    static constexpr int INF = 1 << 28;
    static constexpr int DEFAULT_MAX_COUNT = 300;

    struct TableEntry {
        std::vector<int> dp;
        std::vector<int> prev;
    };

    class RLEDPFailure : public std::runtime_error {
    public:
        using std::runtime_error::runtime_error;
    };

    struct PairHash {
        std::size_t operator()(const std::pair<int, int>& key) const noexcept {
            std::size_t h1 = static_cast<std::size_t>(static_cast<uint32_t>(key.first));
            std::size_t h2 = static_cast<std::size_t>(static_cast<uint32_t>(key.second));
            return h1 ^ (h2 + 0x9e3779b97f4a7c15ULL + (h1 << 6) + (h1 >> 2));
        }
    };

    struct QuadKey {
        int a, b, c, d;
        bool operator==(const QuadKey& other) const noexcept {
            return a == other.a && b == other.b && c == other.c && d == other.d;
        }
    };

    struct QuadHash {
        std::size_t operator()(const QuadKey& key) const noexcept {
            std::size_t h1 = static_cast<std::size_t>(static_cast<uint32_t>(key.a));
            std::size_t h2 = static_cast<std::size_t>(static_cast<uint32_t>(key.b));
            std::size_t h3 = static_cast<std::size_t>(static_cast<uint32_t>(key.c));
            std::size_t h4 = static_cast<std::size_t>(static_cast<uint32_t>(key.d));
            std::size_t h = h1;
            h ^= h2 + 0x9e3779b97f4a7c15ULL + (h << 6) + (h >> 2);
            h ^= h3 + 0x9e3779b97f4a7c15ULL + (h << 6) + (h >> 2);
            h ^= h4 + 0x9e3779b97f4a7c15ULL + (h << 6) + (h >> 2);
            return h;
        }
    };

    std::unordered_map<std::pair<int, int>, TableEntry, PairHash> nonzero_cache;
    std::unordered_map<QuadKey, TableEntry, QuadHash> zero_cache;

    static int sanitize_cost(int cost) {
        return cost > 0 ? cost : INF;
    }

    static int raw_length(const std::vector<int>& lengths, std::size_t idx) {
        if (idx >= lengths.size()) return 0;
        return lengths[idx];
    }

    void ensure_nonzero(TableEntry& entry, int single_cost, int cost16, int required_count) const {
        if (required_count <= 0 && !entry.dp.empty()) return;
        int target = std::max(required_count, DEFAULT_MAX_COUNT);
        if (entry.dp.empty()) {
            entry.dp = {0};
            entry.prev = {0};
        }
        int current = static_cast<int>(entry.dp.size()) - 1;
        if (target <= current) return;
        entry.dp.resize(target + 1, INF);
        entry.prev.resize(target + 1, 0);

        for (int j = current + 1; j <= target; ++j) {
            int best = INF;
            int choice = 0;

            if (single_cost < INF && entry.dp[j - 1] < INF) {
                int cand = entry.dp[j - 1] + single_cost;
                if (cand < best) {
                    best = cand;
                    choice = 1;
                }
            }

            if (cost16 < INF) {
                int add16 = cost16 + 2;
                for (int run = 3; run <= 6 && run <= j; ++run) {
                    int prev_idx = j - run;
                    if (prev_idx < 1) continue;
                    if (entry.dp[prev_idx] >= INF) continue;
                    int cand = entry.dp[prev_idx] + add16;
                    if (cand < best) {
                        best = cand;
                        choice = run;
                    }
                }
            }

            entry.dp[j] = best;
            entry.prev[j] = choice;
        }
    }

    void ensure_zero(TableEntry& entry, int single_cost, int cost16, int cost17, int cost18, int required_count) const {
        if (required_count <= 0 && !entry.dp.empty()) return;
        int target = std::max(required_count, DEFAULT_MAX_COUNT);
        if (entry.dp.empty()) {
            entry.dp = {0};
            entry.prev = {0};
        }
        int current = static_cast<int>(entry.dp.size()) - 1;
        if (target <= current) return;
        entry.dp.resize(target + 1, INF);
        entry.prev.resize(target + 1, 0);

        for (int j = current + 1; j <= target; ++j) {
            int best = INF;
            int choice = 0;

            if (single_cost < INF && entry.dp[j - 1] < INF) {
                int cand = entry.dp[j - 1] + single_cost;
                if (cand < best) {
                    best = cand;
                    choice = 1;
                }
            }

            if (cost17 < INF) {
                int add17 = cost17 + 3;
                for (int run = 3; run <= 10 && run <= j; ++run) {
                    int prev_idx = j - run;
                    if (prev_idx < 0) continue;
                    if (entry.dp[prev_idx] >= INF) continue;
                    int cand = entry.dp[prev_idx] + add17;
                    if (cand < best) {
                        best = cand;
                        choice = run;
                    }
                }
            }

            if (cost18 < INF) {
                int add18 = cost18 + 7;
                for (int run = 11; run <= 138 && run <= j; ++run) {
                    int prev_idx = j - run;
                    if (prev_idx < 0) continue;
                    if (entry.dp[prev_idx] >= INF) continue;
                    int cand = entry.dp[prev_idx] + add18;
                    if (cand < best) {
                        best = cand;
                        choice = run;
                    }
                }
            }

            if (cost16 < INF) {
                int add16 = cost16 + 2;
                for (int run = 3; run <= 6 && run <= j; ++run) {
                    int prev_idx = j - run;
                    if (prev_idx < 1) continue;
                    if (entry.dp[prev_idx] >= INF) continue;
                    int cand = entry.dp[prev_idx] + add16;
                    if (cand < best) {
                        best = cand;
                        choice = -run;
                    }
                }
            }

            entry.dp[j] = best;
            entry.prev[j] = choice;
        }
    }

    TableEntry& get_nonzero_entry(int cost_value, int cost16, int required_count) {
        auto key = std::make_pair(cost_value, cost16);
        auto it = nonzero_cache.find(key);
        if (it == nonzero_cache.end()) {
            it = nonzero_cache.emplace(key, TableEntry{}).first;
        }
        int sanitized_value = sanitize_cost(cost_value);
        int sanitized16 = sanitize_cost(cost16);
        ensure_nonzero(it->second, sanitized_value, sanitized16, required_count);
        return it->second;
    }

    TableEntry& get_zero_entry(int cost0, int cost16, int cost17, int cost18, int required_count) {
        QuadKey key{cost0, cost16, cost17, cost18};
        auto it = zero_cache.find(key);
        if (it == zero_cache.end()) {
            it = zero_cache.emplace(key, TableEntry{}).first;
        }
        int sanitized0 = sanitize_cost(cost0);
        int sanitized16 = sanitize_cost(cost16);
        int sanitized17 = sanitize_cost(cost17);
        int sanitized18 = sanitize_cost(cost18);
        ensure_zero(it->second, sanitized0, sanitized16, sanitized17, sanitized18, required_count);
        return it->second;
    }

    /// sanitizeされていないcostを入れるので注意
    std::vector<RLECode> optimal_parse(const RLEEntry& entry, const std::vector<int>& cl_code_lengths) {
        if (entry.count == 0) return {};
        if (entry.count < 0) {
            throw std::runtime_error("RLE entry count must be non-negative");
        }

        const int INF_CHECK = INF;
        std::vector<RLECode> res;
        res.reserve(entry.count);

        if (entry.value != 0) {
            int cost_value = raw_length(cl_code_lengths, static_cast<std::size_t>(entry.value));
            int cost16 = raw_length(cl_code_lengths, 16);
            auto& table = get_nonzero_entry(cost_value, cost16, entry.count);
            if (entry.count >= table.dp.size() || table.dp[entry.count] >= INF_CHECK) {
                throw RLEDPFailure("DP failed for non-zero value run while encoding CL (value=" + std::to_string(entry.value) + "," +
                                       " count=" + std::to_string(entry.count) + "," +
                                       " cost_value=" + std::to_string(cost_value) + "," +
                                       " cost16=" + std::to_string(cost16) + ")");
            }
            int i = entry.count;
            while (i > 0) {
                int choice = table.prev[i];
                if (choice == 1) {
                    res.push_back({RLECode::LITERAL, entry.value});
                    --i;
                } else if (choice >= 3) {
                    res.push_back({RLECode::PREV_RUN, choice});
                    i -= choice;
                } else {
                    throw std::runtime_error("Invalid DP reconstruction (non-zero)");
                }
            }
        } else {
            int cost0 = raw_length(cl_code_lengths, 0);
            int cost16 = raw_length(cl_code_lengths, 16);
            int cost17 = raw_length(cl_code_lengths, 17);
            int cost18 = raw_length(cl_code_lengths, 18);
            auto& table = get_zero_entry(cost0, cost16, cost17, cost18, entry.count);
            if (entry.count >= table.dp.size() || table.dp[entry.count] >= INF_CHECK) {
                throw RLEDPFailure("DP failed for zero value run while encoding CL (count=" + std::to_string(entry.count) + "," + 
                                    " cost0=" + std::to_string(cost0) + "," +
                                    " cost16=" + std::to_string(cost16) + "," +
                                    " cost17=" + std::to_string(cost17) + "," +
                                    " cost18=" + std::to_string(cost18) + ")");
            }
            int i = entry.count;
            while (i > 0) {
                int choice = table.prev[i];
                if (choice == 1) {
                    res.push_back({RLECode::LITERAL, 0});
                    --i;
                } else if (choice > 0) {
                    res.push_back({RLECode::ZERO_RUN, choice});
                    i -= choice;
                } else if (choice < 0) {
                    int run = -choice;
                    res.push_back({RLECode::PREV_RUN, run});
                    i -= run;
                } else {
                    throw std::runtime_error("Invalid DP reconstruction (zero)");
                }
            }
        }

        std::reverse(res.begin(), res.end());
        return res;
    }

    /// sanitizeされていないcostを入れるので注意
    int compute_optimal_parsing_cost(int value, int count, int cost_value, int cost_16, int cost_17, int cost_18) {
        if (count <= 0) return 0;
        const int INF_CHECK = INF;

        if (value != 0) {
            auto& table = get_nonzero_entry(cost_value, cost_16, count);
            if (count >= table.dp.size() || table.dp[count] >= INF_CHECK) {
                return INF;
            }
            int total = 0;
            int i = count;
            while (i > 0) {
                int choice = table.prev[i];
                if (choice == 1) {
                    total += cost_value;
                    --i;
                } else if (choice >= 3) {
                    total += cost_16 + 2;
                    i -= choice;
                } else {
                    throw std::runtime_error("Invalid DP reconstruction (non-zero cost)");
                }
            }
            return total;
        } else {
            auto& table = get_zero_entry(cost_value, cost_16, cost_17, cost_18, count);
            if (count >= table.dp.size() || table.dp[count] >= INF_CHECK) {
                return INF;
            }
            int total = 0;
            int i = count;
            while (i > 0) {
                int choice = table.prev[i];
                if (choice == 1) {
                    total += cost_value;
                    --i;
                } else if (choice > 0) {
                    if (choice <= 10) {
                        total += cost_17 + 3;
                    } else {
                        total += cost_18 + 7;
                    }
                    i -= choice;
                } else if (choice < 0) {
                    int run = -choice;
                    total += cost_16 + 2;
                    i -= run;
                } else {
                    throw std::runtime_error("Invalid DP reconstruction (zero cost)");
                }
            }
            return total;
        }
    }

    static RLEDPTable& instance() {
        static RLEDPTable table;
        return table;
    }
};

std::vector<int> CL_CODE_ORDER = {
    16, 17, 18, 0, 8, 7, 9, 6,
    10, 5, 11, 4, 12, 3, 13, 2,
    14, 1, 15
};

std::vector<int> compute_huff_code_lengths_from_frequencies(const std::vector<int>& frequencies) {
    // construct from frequencies
    // using a priority queue (min-heap)
    // use above reference-implementation
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> pq;
    std::vector<int> parents(frequencies.size(), -1);
    for (int i = 0; i < frequencies.size(); ++i) {
        if (frequencies[i] > 0) {
            pq.emplace(frequencies[i], i);
        }
    }
    while (pq.size() > 1) {
        auto [freq1, idx1] = pq.top();
        pq.pop();
        auto [freq2, idx2] = pq.top();
        pq.pop();
        parents[idx1] = parents.size();
        parents[idx2] = parents.size();
        pq.emplace(freq1 + freq2, parents.size());
        parents.emplace_back(-1);
    }
    std::vector<int> code_lengths(parents.size(), 0);
    for(int i = parents.size() - 1; i >= 0; --i) {
        if (parents[i] != -1) {
            code_lengths[i] = code_lengths[parents[i]] + 1;
        }
    }
    code_lengths.resize(frequencies.size());
    return code_lengths;
}

std::vector<RLECode> convert_RLEEntry_to_RLECode(const RLEEntry& entry, const std::vector<int>& cl_code_lengths) {
    return RLEDPTable::instance().optimal_parse(entry, cl_code_lengths);
}

std::vector<RLEEntry> length_RLE(const std::vector<int>& vec);

std::vector<int> get_optimal_cl_code_lengths(const std::vector<int>& literal_code_lengths, const std::vector<int>& distance_code_lengths) {
    std::vector<int> concat = literal_code_lengths;
    concat.insert(concat.end(), distance_code_lengths.begin(), distance_code_lengths.end());
    auto rle_entries = length_RLE(concat);

    constexpr int MAX_CL_CODE_LENGTH = 10;
    constexpr int INF = 1 << 28;

    auto get_tree_cost = [&](int code_length){
        if (code_length == 0) return 0;
        return (1 << (MAX_CL_CODE_LENGTH - code_length));
    };

    std::vector<std::vector<int>> rle_entries_by_code(19);
    for (const auto& entry : rle_entries) {
        rle_entries_by_code[entry.value].emplace_back(entry.count);
    }

    std::pair<int, std::vector<int>> best_result = {INF, {}};

    int min_hclen = 0;
    for (int i = 0; i < 16; ++i) {
        if (!rle_entries_by_code[CL_CODE_ORDER[i + 3]].empty()) {
            min_hclen = i + 1;
        }
    }

    for (int cost_16 = 0; cost_16 <= MAX_CL_CODE_LENGTH; ++cost_16) {
        for (int cost_17 = 0; cost_17 <= MAX_CL_CODE_LENGTH; ++cost_17) {
            for (int cost_18 = 0; cost_18 <= MAX_CL_CODE_LENGTH; ++cost_18) {
                // dp[i][j]: code i まで決めて、ハフマン符号の占有率が j
                // TODO: cl codeの5bits制限も考える
                std::vector<std::vector<int>> dp(17, std::vector<int>((1 << MAX_CL_CODE_LENGTH) + 1, INF));
                std::vector<std::vector<int>> prev(17, std::vector<int>((1 << MAX_CL_CODE_LENGTH) + 1, -1));
                int cost_start = get_tree_cost(cost_16) + get_tree_cost(cost_17) + get_tree_cost(cost_18);
                if (cost_start >= (1 << MAX_CL_CODE_LENGTH)) {
                    continue;
                }
                dp[0][cost_start] = 0;
                for (int i = 0; i < 16; ++i) {
                    int cl_i = CL_CODE_ORDER[i + 3];
                    std::vector<int> RLE_part_cost(MAX_CL_CODE_LENGTH + 1, 0);
                    for (int cl = 0; cl <= MAX_CL_CODE_LENGTH; ++cl) {
                        for (auto count : rle_entries_by_code[cl_i]) {
                            RLE_part_cost[cl] += RLEDPTable::instance().compute_optimal_parsing_cost(cl_i, count, cl, cost_16, cost_17, cost_18);
                            RLE_part_cost[cl] = std::min(RLE_part_cost[cl], INF); // overflow 対策
                        }
                    }
                    for (int j = cost_start; j < (1 << MAX_CL_CODE_LENGTH); ++j) {
                        if (dp[i][j] == INF) continue;
                        for (int cl = 0; cl <= MAX_CL_CODE_LENGTH; ++cl) {
                            int new_j = j + get_tree_cost(cl);
                            if (new_j > (1 << MAX_CL_CODE_LENGTH)) continue;
                            int cost = dp[i][j] + RLE_part_cost[cl];
                            if (cost < dp[i + 1][new_j]) {
                                dp[i + 1][new_j] = cost;
                                prev[i + 1][new_j] = cl;
                            }
                        }
                    }
                }

                int best_cost = 2 * INF;
                int i = 16;
                int j = (1 << MAX_CL_CODE_LENGTH);
                for (int k = min_hclen; k <= 16; ++k) {
                    if (dp[k][j] + 5 * k < best_cost) {
                        best_cost = dp[k][j] + 5 * k;
                        i = k;
                    }
                }
                if (best_cost >= INF) {
                    continue;
                }
                std::vector<int> cl_code_lengths(19, 0);
                while (i > 0) {
                    int cl = prev[i][j];
                    if (cl == -1) {
                        throw std::runtime_error("Invalid DP reconstruction for CL code lengths" + std::to_string(cost_16) + " " + std::to_string(cost_17) + " " + std::to_string(cost_18) + " : " + std::to_string(i) + " " + std::to_string(j));
                    }
                    cl_code_lengths[CL_CODE_ORDER[i + 2]] = cl;
                    j -= get_tree_cost(cl);
                    --i;
                }
                cl_code_lengths[16] = cost_16;
                cl_code_lengths[17] = cost_17;
                cl_code_lengths[18] = cost_18;
                if (best_cost < best_result.first) {
                    best_result = {best_cost, cl_code_lengths};
                }
            }
        }
    }
    return best_result.second;
}


Token read_one_token(std::istream& in) {
    char type;
    in >> type;
    if (type == 'L') {
        int literal;
        in >> literal;
        Token tok = 
            { Token::LITERAL, .literal = static_cast<unsigned char>(literal) };
        return tok;
    } else if (type == 'M') {
        int length, distance;
        in >> length >> distance;
        Token tok = { Token::COPY, .pair = { length, distance } };
        return tok;
    } else {
        throw std::runtime_error("Invalid token type");
    }
}

int convert_length_value_to_code(int length) {
    if (length <= 10) return 257 + (length - 3);
    else if (length <= 18) return 265 + (length - 11) / 2;
    else if (length <= 34) return 269 + (length - 19) / 4;
    else if (length <= 66) return 273 + (length - 35) / 8;
    else if (length <= 130) return 277 + (length - 67) / 16;
    else if (length <= 257) return 281 + (length - 131) / 32;
    else if (length == 258) return 285;
    else throw std::runtime_error("Invalid length");
}
int convert_distance_value_to_code(int distance) {
    if (distance <= 4) return distance - 1;
    else if (distance <= 8) return 4 + (distance - 5) / 2;
    else if (distance <= 16) return 6 + (distance - 9) / 4;
    else if (distance <= 32) return 8 + (distance - 17) / 8;
    else if (distance <= 64) return 10 + (distance - 33) / 16;
    else if (distance <= 128) return 12 + (distance - 65) / 32;
    else if (distance <= 256) return 14 + (distance - 129) / 64;
    else if (distance <= 512) return 16 + (distance - 257) / 128;
    else if (distance <= 1024) return 18 + (distance - 513) / 256;
    else if (distance <= 2048) return 20 + (distance - 1025) / 512;
    else if (distance <= 4096) return 22 + (distance - 2049) / 1024;
    else if (distance <= 8192) return 24 + (distance - 4097) / 2048;
    else if (distance <= 16384) return 26 + (distance - 8193) / 4096;
    else if (distance <= 32768) return 28 + (distance - 16385) / 8192;
    else throw std::runtime_error("Invalid distance");
}
int num_additional_bits_for_len(int length) {
    if (length <= 10) return 0;
    else if (length <= 18) return 1;
    else if (length <= 34) return 2;
    else if (length <= 66) return 3;
    else if (length <= 130) return 4;
    else if (length <= 257) return 5;
    else if (length == 258) return 0;
    else throw std::runtime_error("Invalid length");
}
int num_additional_bits_for_dist(int distance) {
    if (distance <= 4) return 0;
    else if (distance <= 8) return 1;
    else if (distance <= 16) return 2;
    else if (distance <= 32) return 3;
    else if (distance <= 64) return 4;
    else if (distance <= 128) return 5;
    else if (distance <= 256) return 6;
    else if (distance <= 512) return 7;
    else if (distance <= 1024) return 8;
    else if (distance <= 2048) return 9;
    else if (distance <= 4096) return 10;
    else if (distance <= 8192) return 11;
    else if (distance <= 16384) return 12;
    else if (distance <= 32768) return 13;
    else throw std::runtime_error("Invalid distance");
}

static const int LENGTH_BASE[29] = {
    3, 4, 5, 6, 7, 8, 9, 10,
    11, 13, 15, 17,
    19, 23, 27, 31,
    35, 43, 51, 59,
    67, 83, 99, 115,
    131, 163, 195, 227,
    258
};

static const int LENGTH_EXTRA[29] = {
    0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1,
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    0
};

static const int DIST_BASE[30] = {
    1, 2, 3, 4, 5, 7, 9, 13,
    17, 25, 33, 49,
    65, 97, 129, 193,
    257, 385, 513, 769,
    1025, 1537, 2049, 3073,
    4097, 6145, 8193, 12289,
    16385, 24577
};

static const int DIST_EXTRA[30] = {
    0, 0, 0, 0, 1, 1, 2, 2,
    3, 3, 4, 4,
    5, 5, 6, 6,
    7, 7, 8, 8,
    9, 9, 10, 10,
    11, 11, 12, 12,
    13, 13
};

inline int length_base_for_code(int length_code) {
    if (length_code < 257 || length_code > 285) {
        throw std::runtime_error("Invalid length code");
    }
    return LENGTH_BASE[length_code - 257];
}

inline int length_extra_for_code(int length_code) {
    if (length_code < 257 || length_code > 285) {
        throw std::runtime_error("Invalid length code");
    }
    return LENGTH_EXTRA[length_code - 257];
}

inline int distance_base_for_code(int distance_code) {
    if (distance_code < 0 || distance_code > 29) {
        throw std::runtime_error("Invalid distance code");
    }
    return DIST_BASE[distance_code];
}

inline int distance_extra_for_code(int distance_code) {
    if (distance_code < 0 || distance_code > 29) {
        throw std::runtime_error("Invalid distance code");
    }
    return DIST_EXTRA[distance_code];
}

std::vector<RLEEntry> length_RLE(const std::vector<int>& vec) {
    std::vector<RLEEntry> res;
    int prev = -1;
    int run_length = 0;
    for(int i = 0; i < vec.size() + 1; ++i) {
        int value = (i == vec.size()) ? -1 : vec[i];
        if (value == prev) {
            run_length++;
        } else {
            if (prev != -1 ) {
                res.push_back({prev, run_length});
            }
            prev = value;
            run_length = 1;
        }
    }
    return res;
}

struct CompressedBlock : public Block {
    std::vector<Token> tokens;
    virtual int get_literal_code_length(int literal_code) const = 0;
    virtual int get_distance_code_length(int distance_code) const = 0;
};
    

std::vector<RLECode> compute_RLE_encoded_representation(const std::vector<int>& literal_code_lengths, const std::vector<int>& distance_code_lengths, const std::vector<int>& cl_code_lengths) {
    // Note: This run-length encoding is not optimal.
    // Each run-length encoded symbol will be compressed using huffman codes, so acutually we should consider it.
    std::vector<int> concat = literal_code_lengths;
    concat.insert(concat.end(), distance_code_lengths.begin(), distance_code_lengths.end());
    auto rle_entries = length_RLE(concat);
    std::vector<RLECode> rle_codes;
    for (const auto& entry : rle_entries) {
        auto codes = convert_RLEEntry_to_RLECode(entry, cl_code_lengths);
        rle_codes.insert(rle_codes.end(), codes.begin(), codes.end());
    }
    return rle_codes;
}

struct StoredBlock : public Block {
    std::vector<int> data;
    void dump_string(std::ostream& out) const {
        out << bfinal << ' ' << 0b00 << '\n';
        out << data.size() << '\n';
        for (size_t i = 0; i < data.size(); ++i) {
            out << data[i] << (i + 1 == data.size() ? "\n" : " ");
        }
    }
    int bit_length() const override {
        // Acutually the data after bfinal and btype is byte-aligned.
        // Here we just return the bit length as if it were not aligned.
        return 3 + 16 + 16 + data.size() * 8;
    }
    std::vector<int> get_string(const std::vector<int>& context) const override {
        return data;
    }
    static StoredBlock load_from_stream(std::istream& in) {
        StoredBlock block;
        size_t len;
        in >> len;
        block.data.resize(len);
        for (size_t i = 0; i < len; ++i) {
            int byte_val;
            in >> byte_val;
            block.data[i] = static_cast<unsigned char>(byte_val);
        }
        return block;
    }
};

struct DynamicHuffmanBlock;

struct FixedHuffmanBlock : public CompressedBlock {
    void dump_string(std::ostream& out) const {
        out << bfinal << ' ' << 0b01 << '\n';
        out << tokens.size() << '\n';
        for (int i = 0; i < tokens.size(); ++i) {
            out << tokens[i].get_string() << (i + 1 == tokens.size() ? "\n" : " ");
        }
    }
    int bit_length() const override {
        // std::cout << "num factors: " << tokens.size() << std::endl;
        int length = 3;
        for (const auto& token : tokens) {
            if (token.type == Token::LITERAL) {
                length += get_literal_code_length(token.literal);
            } else {
                int lit_code = convert_length_value_to_code(token.pair.length);
                length += get_literal_code_length(lit_code);
                length += num_additional_bits_for_len(token.pair.length);
                int dist_code = convert_distance_value_to_code(token.pair.distance);
                length += get_distance_code_length(dist_code);
                length += num_additional_bits_for_dist(token.pair.distance);
            }
        }
        length += get_literal_code_length(256);
        return length;
    }
    std::vector<int> get_string(const std::vector<int>& context) const override {
        std::vector<int> res;
        for (const auto& token : tokens) {
            if (token.type == Token::LITERAL) {
                res.push_back(token.literal);
            } else {
                int start = res.size() - token.pair.distance;
                for (int i = 0; i < token.pair.length; ++i) {
                    if (start + i >= 0 && start + i < res.size()) {
                        res.push_back(res[start + i]);
                    } else if (start + i >= 0 && start + i < context.size()) {
                        res.push_back(context[start + i]);
                    } else {
                        throw std::runtime_error("COPY distance out of bounds");
                    }
                }
            }
        }
        return res;
    }
    int get_literal_code_length(int literal_code) const override {
        if (literal_code <= 143) return 8;
        else if (literal_code <= 255) return 9;
        else if (literal_code <= 279) return 7;
        else if (literal_code <= 287) return 8;
        else throw std::runtime_error("Invalid literal");
    }
    int get_distance_code_length(int distance_code) const override {
        return 5;
    }
    static FixedHuffmanBlock load_from_stream(std::istream& in) {
        FixedHuffmanBlock block;
        size_t len;
        in >> len;
        block.tokens.resize(len);
        for (size_t i = 0; i < len; ++i) {
            block.tokens[i] = read_one_token(in);
        }
        return block;
    }
    DynamicHuffmanBlock to_dynamic_huffman_block() const;
};

struct DynamicHuffmanBlock : public CompressedBlock {
    std::vector<int> literal_code_lengths;
    std::vector<int> distance_code_lengths;
    std::vector<int> cl_code_lengths; // len(cl_code_lengths) == 19, stored in normal order
    void dump_string(std::ostream& out) const {
        out << bfinal << ' ' << 0b10 << '\n';
        for (size_t i = 0; i < cl_code_lengths.size(); ++i) {
            out << cl_code_lengths[i] << (i + 1 == cl_code_lengths.size() ? "\n" : " ");
        }
        out << literal_code_lengths.size() << '\n';
        for (size_t i = 0; i < literal_code_lengths.size(); ++i) {
            out << literal_code_lengths[i] << (i + 1 == literal_code_lengths.size() ? "\n" : " ");
        }
        out << distance_code_lengths.size() << '\n';
        for (size_t i = 0; i < distance_code_lengths.size(); ++i) {
            out << distance_code_lengths[i] << (i + 1 == distance_code_lengths.size() ? "\n" : " ");
        }
        out << tokens.size() << '\n';
        for (int i = 0; i < tokens.size(); ++i) {
            out << tokens[i].get_string() << (i + 1 == tokens.size() ? "\n" : " ");
        }
    }
    auto get_optimal_cl_code_lengths() const {
        std::vector<RLECode> rle_codes = compute_RLE_encoded_representation(literal_code_lengths, distance_code_lengths, cl_code_lengths);
        std::vector<int> cl_frequencies(19, 0);
        for (const auto& code : rle_codes) {
            cl_frequencies[code.id()]++;
        }
        auto res = compute_huff_code_lengths_from_frequencies(cl_frequencies);
        return compute_huff_code_lengths_from_frequencies(cl_frequencies);
    }
    int bit_length() const override {
        // std::cout << "num factors: " << tokens.size() << std::endl;
        int length = 3; // bfinal + btype
        // HLIT, HDIST, HCLEN
        length += 5 + 5 + 4;
        int hclen = 0;
        for (int i = 18; i >= 0; --i) {
            if (cl_code_lengths[CL_CODE_ORDER[i]] > 0) {
                hclen = i + 1;
                break;
            }
        }
        length += hclen * 3;
        std::vector<RLECode> rle_codes = compute_RLE_encoded_representation(literal_code_lengths, distance_code_lengths, cl_code_lengths);
        for (auto& code : rle_codes) {
            length += cl_code_lengths[code.id()];
            length += code.num_additional_bits();
        }
        // body
        for(auto tok : tokens) {
            if (tok.type == Token::LITERAL) {
                length += literal_code_lengths[tok.literal];
            } else { // COPY
                int lit_code = convert_length_value_to_code(tok.pair.length);
                int distance_code = convert_distance_value_to_code(tok.pair.distance);
                length += literal_code_lengths[lit_code];
                length += num_additional_bits_for_len(tok.pair.length);
                length += distance_code_lengths[distance_code];
                length += num_additional_bits_for_dist(tok.pair.distance);
            }
        }
        length += get_literal_code_length(256);
        return length;
    }
    std::vector<unsigned char> encode_to_embed_bytes() const {
        auto result = encode_to_bytes();
        return get_embed_string_bytes(result.first);
    }
    int bit_length_with_added_size() const {
        auto result = encode_to_bytes();
        std::size_t added_bytes = compute_added_bytes_for_embed(result.first);
        long long total_bits = static_cast<long long>(result.second) + static_cast<long long>(added_bytes) * 8LL;
        if (total_bits > std::numeric_limits<int>::max()) {
            throw std::overflow_error("bit_length_with_added_size overflow");
        }
        return static_cast<int>(total_bits);
    }
    std::pair<std::vector<unsigned char>, int> encode_to_bytes() const {
        if (literal_code_lengths.size() < 257 || literal_code_lengths.size() > 286) {
            throw std::runtime_error("Invalid literal code length table size");
        }
        if (distance_code_lengths.empty() || distance_code_lengths.size() > 32) {
            throw std::runtime_error("Invalid distance code length table size");
        }
        if (cl_code_lengths.size() != 19) {
            throw std::runtime_error("Invalid code-length alphabet size");
        }

        BitWriter writer;
        writer.write_bits(bfinal ? 1u : 0u, 1);
        writer.write_bits(0b10u, 2);

        int hlit = static_cast<int>(literal_code_lengths.size()) - 257;
        if (hlit < 0 || hlit > 31) {
            throw std::runtime_error("HLIT out of range");
        }
        writer.write_bits(static_cast<uint32_t>(hlit), 5);

        int hdist = static_cast<int>(distance_code_lengths.size()) - 1;
        if (hdist < 0 || hdist > 31) {
            throw std::runtime_error("HDIST out of range");
        }
        writer.write_bits(static_cast<uint32_t>(hdist), 5);

        int hclen = 4;
        for (int i = 18; i >= 0; --i) {
            if (cl_code_lengths[CL_CODE_ORDER[i]] > 0) {
                hclen = i + 1;
                break;
            }
        }
        if (hclen < 4) {
            hclen = 4;
        }
        writer.write_bits(static_cast<uint32_t>(hclen - 4), 4);
        for (int i = 0; i < hclen; ++i) {
            int symbol = CL_CODE_ORDER[i];
            int len = cl_code_lengths[symbol];
            if (len < 0 || len > 7) {
                throw std::runtime_error("Invalid CL code length");
            }
            writer.write_bits(static_cast<uint32_t>(len), 3);
        }

        auto cl_codes = build_reversed_canonical_codes(cl_code_lengths);
        std::vector<RLECode> rle_codes = compute_RLE_encoded_representation(
            literal_code_lengths, distance_code_lengths, cl_code_lengths);
        for (const auto& code : rle_codes) {
            int symbol = code.id();
            if (symbol < 0 || symbol >= static_cast<int>(cl_code_lengths.size())) {
                throw std::runtime_error("CL symbol out of range");
            }
            int len = cl_code_lengths[symbol];
            if (len <= 0) {
                throw std::runtime_error("Unused CL symbol referenced");
            }
            writer.write_bits(cl_codes[symbol], len);
            if (code.type == RLECode::PREV_RUN) {
                if (code.value < 3 || code.value > 6) {
                    throw std::runtime_error("Invalid PREV_RUN length");
                }
                writer.write_bits(static_cast<uint32_t>(code.value - 3), 2);
            } else if (code.type == RLECode::ZERO_RUN) {
                if (code.value <= 10) {
                    writer.write_bits(static_cast<uint32_t>(code.value - 3), 3);
                } else {
                    writer.write_bits(static_cast<uint32_t>(code.value - 11), 7);
                }
            }
        }

        auto literal_codes = build_reversed_canonical_codes(literal_code_lengths);
        auto distance_codes = build_reversed_canonical_codes(distance_code_lengths);

        for (const auto& tok : tokens) {
            if (tok.type == Token::LITERAL) {
                int symbol = tok.literal;
                if (symbol < 0 || symbol >= static_cast<int>(literal_code_lengths.size())) {
                    throw std::runtime_error("Literal symbol out of range");
                }
                int len = literal_code_lengths[symbol];
                if (len <= 0) {
                    throw std::runtime_error("Literal code has zero length");
                }
                writer.write_bits(literal_codes[symbol], len);
            } else {
                int length_code = convert_length_value_to_code(tok.pair.length);
                if (length_code >= static_cast<int>(literal_code_lengths.size()) ||
                    literal_code_lengths[length_code] <= 0) {
                    throw std::runtime_error("Length code undefined");
                }
                int len_bits = literal_code_lengths[length_code];
                writer.write_bits(literal_codes[length_code], len_bits);
                int extra_len_bits = length_extra_for_code(length_code);
                if (extra_len_bits > 0) {
                    int base = length_base_for_code(length_code);
                    int extra_value = tok.pair.length - base;
                    if (extra_value < 0 || extra_value >= (1 << extra_len_bits)) {
                        throw std::runtime_error("Length extra bits out of range");
                    }
                    writer.write_bits(static_cast<uint32_t>(extra_value), extra_len_bits);
                }

                int dist_code = convert_distance_value_to_code(tok.pair.distance);
                if (dist_code >= static_cast<int>(distance_code_lengths.size()) ||
                    distance_code_lengths[dist_code] <= 0) {
                    throw std::runtime_error("Distance code undefined");
                }
                int dist_len = distance_code_lengths[dist_code];
                writer.write_bits(distance_codes[dist_code], dist_len);
                int extra_dist_bits = distance_extra_for_code(dist_code);
                if (extra_dist_bits > 0) {
                    int base = distance_base_for_code(dist_code);
                    int extra_value = tok.pair.distance - base;
                    if (extra_value < 0 || extra_value >= (1 << extra_dist_bits)) {
                        throw std::runtime_error("Distance extra bits out of range");
                    }
                    writer.write_bits(static_cast<uint32_t>(extra_value), extra_dist_bits);
                }
            }
        }

        if (literal_code_lengths.size() <= 256 || literal_code_lengths[256] <= 0) {
            throw std::runtime_error("End-of-block code undefined");
        }
        writer.write_bits(literal_codes[256], literal_code_lengths[256]);

        int total_bit_length = writer.get_bit_length();
        auto bytes = writer.take_bytes();
        return {std::move(bytes), total_bit_length};
    }

    // TODO: return f"https://deflate-viz.pages.dev?deflate={base64.b64encode(deflate).decode().replace('+', '%2B').replace('/', '%2F').replace('=', '%3D')}"
    std::string viz_deflate_url() const {
        auto [deflate, bitlen] = encode_to_bytes();
        std::string base64;
        static const char* base64_chars =
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
            "0123456789+/";
        int val = 0, valb = -6;
        for (unsigned char c : deflate) {
            val = (val << 8) + c;
            valb += 8;
            while (valb >= 0) {
                base64.push_back(base64_chars[(val >> valb) & 0x3F]);
                valb -= 6;
            }
        }
        if (valb > -6) {
            base64.push_back(base64_chars[((val << 8) >> (valb + 8)) & 0x3F]);
        }
        while (base64.size() % 4) {
            base64.push_back('=');
        }
        std::string url = "https://deflate-viz.pages.dev?deflate=";
        for (char c : base64) {
            if (c == '+') url += "%2B";
            else if (c == '/') url += "%2F";
            else if (c == '=') url += "%3D";
            else url += c;
        }
        return url;
    }

    std::vector<int> get_string(const std::vector<int>& context) const override {
        std::vector<int> res;
        res.reserve(context.size() + tokens.size()); // 任意の最適化

        for (const auto& token : tokens) {
            if (token.type == Token::LITERAL) {
                res.push_back(token.literal);
                continue;
            }

            const int len = token.pair.length;
            const int dist = token.pair.distance;

            // 総復号済み長。COPY はここから距離で遡る
            const int total = static_cast<int>(context.size() + res.size());
            if (dist <= 0 || dist > total) {
                throw std::runtime_error("COPY distance out of bounds");
            }

            // 参照開始位置は「context + res」の連結列のインデックス
            int pos = total - dist;

            for (int k = 0; k < len; ++k, ++pos) {
                if (pos < static_cast<int>(context.size())) {
                    // 参照元は context
                    res.push_back(context[pos]);
                } else {
                    // 参照元は res
                    int rpos = pos - static_cast<int>(context.size());
                    if (rpos < 0 || rpos >= static_cast<int>(res.size())) {
                        // オーバーラップ COPY に対しても逐次 push で増えるため
                        // 理論上ここは到達しないが防御的に検査
                        throw std::runtime_error("COPY source not yet available");
                    }
                    res.push_back(res[rpos]);
                }
            }
        }
        return res;
    }
    int get_literal_code_length(int literal_code) const override {
        return (literal_code >= literal_code_lengths.size() || literal_code_lengths[literal_code] == 0)
                ? 1e9
                : literal_code_lengths[literal_code];
    }
    int get_distance_code_length(int distance_code) const override {
        return (distance_code >= distance_code_lengths.size() || distance_code_lengths[distance_code] == 0)
                ? 1e9
                : distance_code_lengths[distance_code];
    }
    /// lit/dist のみ cl_code_length は初期化しない
    void reset_code_length_as_static_block() {
        literal_code_lengths.resize(288, 0);
        for (int i = 0; i <= 143; ++i) literal_code_lengths[i] = 8;
        for (int i = 144; i <= 255; ++i) literal_code_lengths[i] = 9;
        for (int i = 256; i <= 279; ++i) literal_code_lengths[i] = 7;
        for (int i = 280; i <= 287; ++i) literal_code_lengths[i] = 8;
        distance_code_lengths.resize(32, 5);
    }
    static DynamicHuffmanBlock load_from_stream(std::istream& in) {
        DynamicHuffmanBlock block;
        size_t hlit, hdist;
        block.cl_code_lengths.resize(19, 0);
        for (size_t i = 0; i < 19; ++i) {
            in >> block.cl_code_lengths[i];
        }
        in >> hlit;
        block.literal_code_lengths.resize(hlit);
        for (size_t i = 0; i < hlit; ++i) {
            in >> block.literal_code_lengths[i];
        }
        in >> hdist;
        block.distance_code_lengths.resize(hdist);
        for (size_t i = 0; i < hdist; ++i) {
            in >> block.distance_code_lengths[i];
        }
        size_t len;
        in >> len;
        block.tokens.resize(len);
        for (size_t i = 0; i < len; ++i) {
            block.tokens[i] = read_one_token(in);
        }
        return block;
    }
    FixedHuffmanBlock to_fixed_huffman_block() const {
        FixedHuffmanBlock block;
        block.bfinal = bfinal;
        block.tokens = tokens;
        return block;
    }

    /// It does not work if context is not emopty.
    std::pair<DynamicHuffmanBlock, FixedHuffmanBlock> split_at_position(int split_pos) const {
        auto text = get_string({});
        if (split_pos < 0 || split_pos > text.size()) {
            throw std::runtime_error("Invalid split position");
        }
        DynamicHuffmanBlock first;
        first.bfinal = false;
        first.literal_code_lengths = literal_code_lengths;
        first.distance_code_lengths = distance_code_lengths;
        first.cl_code_lengths = cl_code_lengths;
        FixedHuffmanBlock second;
        second.bfinal = bfinal;
        
        int text_pos = 0;
        for (auto tok : tokens) {
            int next_pos = text_pos + (tok.type == Token::LITERAL ? 1 : tok.pair.length);
            if (next_pos <= split_pos) {
                first.tokens.push_back(tok);
                text_pos = next_pos;
            } else if (text_pos >= split_pos) {
                second.tokens.push_back(tok);
            } else {
                // split within this token
                if (tok.type == Token::LITERAL) {
                    // should not happen
                    throw std::runtime_error("Cannot split within a literal token");
                } else {
                    int len1 = split_pos - text_pos;
                    int len2 = tok.pair.length - len1;
                    if (len1 > 0) {
                        if (len1 >= 3) {
                            first.tokens.push_back({Token::COPY, .pair = {len1, tok.pair.distance}});
                        }
                        else {
                            for (int i = 0; i < len1; ++i) {
                                first.tokens.push_back({Token::LITERAL, .literal = static_cast<unsigned char>(text[text_pos + i])});
                            }
                        }
                    }
                    if (len2 > 0) {
                        if (len2 >= 3) {
                            second.tokens.push_back({Token::COPY, .pair = {len2, tok.pair.distance}});
                        }
                        else {
                            for (int i = 0; i < len2; ++i) {
                                second.tokens.push_back({Token::LITERAL, .literal = static_cast<unsigned char>(text[split_pos + i])});
                            }
                        }
                    }
                    text_pos = next_pos;
                }
            }
        }
        return std::make_pair(first, second);
    }
};

DynamicHuffmanBlock FixedHuffmanBlock::to_dynamic_huffman_block() const {
    DynamicHuffmanBlock block;
    block.bfinal = bfinal;
    block.tokens = tokens;
    block.literal_code_lengths.resize(288, 0);
    for (int i = 0; i <= 143; ++i) block.literal_code_lengths[i] = 8;
    for (int i = 144; i <= 255; ++i) block.literal_code_lengths[i] = 9;
    for (int i = 256; i <= 279; ++i) block.literal_code_lengths[i] = 7;
    for (int i = 280; i <= 287; ++i) block.literal_code_lengths[i] = 8;
    block.distance_code_lengths.resize(32, 0);
    for (int i = 0; i <= 31; ++i) block.distance_code_lengths[i] = 5;
    block.cl_code_lengths.resize(19, 5);
    return block;
}

static std::unique_ptr<Block> load_block_from_stream(std::istream& in) {
    int bfinal_int, btype;
    in >> bfinal_int >> btype;
    bool bfinal = (bfinal_int != 0);
    if (btype == 0b00) {
        auto blk = std::make_unique<StoredBlock>(StoredBlock::load_from_stream(in));
        blk->bfinal = bfinal;
        return blk;
    } else if (btype == 0b01) {
        auto blk = std::make_unique<FixedHuffmanBlock>(FixedHuffmanBlock::load_from_stream(in));
        blk->bfinal = bfinal;
        return blk;
    } else if (btype == 0b10) {
        auto blk = std::make_unique<DynamicHuffmanBlock>(DynamicHuffmanBlock::load_from_stream(in));
        blk->bfinal = bfinal;
        return blk;
    } else {
        throw std::runtime_error("Unsupported block type");
    }
}
