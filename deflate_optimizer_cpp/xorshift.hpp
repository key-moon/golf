#pragma once
namespace XorShift{
  uint64_t rnd_val = 0xdeadbeefcafebabe;
  uint64_t rand(){ rnd_val ^= rnd_val << 7; rnd_val ^= rnd_val >> 9; return rnd_val; }
  double rand_double(){ return double(rand()) / UINT64_MAX; }
  template<int N>
  int randn(){ return (uint64_t(uint32_t(rand())) * N) >> 32; }
  int randn(int n){ return (uint64_t(uint32_t(rand())) * n) >> 32; }
  std::vector<int> rand_perm(int n){
    std::vector<int> v(n);
    std::iota(v.begin(), v.end(), 0);
    for(int i = n - 1; i >= 1; --i){
      int j = randn(i + 1);
      std::swap(v[i], v[j]);
    }
    return v;
  }
  template<typename T>
  void shuffle(std::vector<T>& v){
    int n = v.size();
    for(int i = n - 1; i >= 1; --i){
      int j = randn(i + 1);
      std::swap(v[i], v[j]);
    }
  }
};
