# best: 64(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 74(xsot ovs att joking mewheni), 76(natte), 80(dbdr), 85(Yuchen20), 86(kabutack)
# ============================= 64 =============================
# lambda g:[[(a:=553**(99>v))%5]+[(a:=v*a%1662)%5for _ in g[0][1:]]for v in(35,1225,1260)] <= kasu
p=lambda g:[(a:=v//237)and[6&(a:=v*a%1662)%5-7for _ in g[0]]for v in[8405,235057,254381]]
# mapping = {0: 0, 2: 2, 3: 4}

#  エンコードしたいもの: 初期値とb 冷静になると a:=a*b%m を要素にするなら初期値の一個前か
#   (1,   35) -> (  95,   35) or   (1,  95) -> (  35,  95)
# (553, 1225) -> (1501, 1225) or (553, 715) -> ( 991, 715)
# (553,   35) -> (1013,   35) or (553,  95) -> (1073,  95)
# 結局これらは mod 1662とられるので、中国剰余定理みたいな埋め込み方をしていい

# EMBED = [(95, 35), (1501, 1225), (1013, 35)]
# [(e%1662, e//788) for e in [28349, 965461, 27605]] == [(95, 35), (1501, 1225), (1013, 35)]
# EMBED = [(35, 95), (1225, 1501), (35, 1013)]
# [(e%1662, e//210) for e in [19979, 315343, 212771]] == [(35, 95), (1225, 1501), (35, 1013)]
# EMBED = [(35, 95), (991, 715), (1073, 95)]
# [(e%1662, e//728) for e in [69839, 521197, 69215]] == [(35, 95), (991, 715), (1073, 95)]
# EMBED = [(95, 35), (715, 991), (95, 1073)]
# [(e%1662, e//237) for e in [8405, 235057, 254381]] == [(95, 35), (715, 991), (95, 1073)]

# MOD = 1662
# EMBED = [(95, 35), (715, 991), (95, 1073)]
# for div in range(2, 1000):
#   embedded = []
#   ok = True
#   for a, b in EMBED:
#     val = a + max(0, (div * b - a) // MOD * MOD)
#     while val // div <= b:
#       if val // div == b:
#         embedded.append(val)
#         break
#       val += MOD
#     else:
#       break
#   else:
#     print(f"[(e%{MOD}, e//{div}) for e in {embedded}] == {EMBED}")

# 35**i%1662%5: [1, 0, 0, 0, 1, 3, 3, 3, 1, 0, 0, 0]
# 32**i%2821&12: [0, 0, 0, 8, 0, 0, 0, 8, 12, 12, 12, 8]
# 32**i%2821&384: [0, 0, 0, 128, 384, 384, 384, 128, 0, 0, 0, 128]
# 818**i%2862&1056: [0, 32, 32, 32, 0, 1056, 1056, 1056, 0, 32, 32, 32]
# 512**i%3240&1536: [0, 512, 512, 512, 0, 1536, 1536, 1536, 0, 512, 512, 512]
# 128**i%3393&2056: [0, 0, 2056, 0, 0, 0, 2056, 8, 8, 8, 2056, 0]
# 1346**i%4177&520: [0, 0, 0, 520, 0, 0, 0, 520, 8, 8, 8, 520]
# 1519**i%4614&68: [0, 68, 64, 64, 64, 68, 0, 0, 0, 68, 0, 0]
# 1939**i%4909&2052: [0, 0, 0, 2048, 4, 4, 4, 2048, 4, 4, 4, 2048]
# 5523**i%8354&520: [0, 0, 0, 520, 0, 0, 0, 520, 8, 8, 8, 520]
# 6133**i%9228&68: [0, 68, 64, 64, 64, 68, 0, 0, 0, 68, 0, 0]

# import math

# a = [2, 0, 0, 0, 2, 0, 0, 0, 2, 1, 1, 1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 1, 1, 1]
# ab = bytes(a)

# def _trial_factor(n):
#   if n <= 0: raise ValueError("n must be >0")
#   f = {}
#   while n % 2 == 0: f[2] = f.get(2, 0) + 1; n //= 2
#   p = 3
#   while p * p <= n:
#     while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
#     p += 2
#   if n > 1: f[n] = f.get(n, 0) + 1
#   return f

# def _lcm(a, b): return a // math.gcd(a, b) * b

# def carmichael_lambda(n):
#   if n == 1: return 1
#   res = 1
#   for p, e in _trial_factor(n).items():
#     if p == 2:
#       comp = 1 if e == 1 else 2 if e == 2 else 1 << (e - 2)
#     else:
#       comp = pow(p, e - 1) * (p - 1)
#     res = _lcm(res, comp)
#   return res

# def check_seq(seq: list[int]):
#   s = {*seq}
#   if len(s) != 3: return False
#   zero = max(seq, key=seq.count)
#   if seq.count(zero) != 6:
#     return False
#   two = (s-{zero}).pop()
#   if seq.count(two) != 3:
#     return False
#   one = sum(s) - zero - two
#   mp = { zero: 0, one: 1, two: 2 }
#   if bytes([mp[o] for o in seq]) in ab: return True
#   mp = { zero: 0, one: 2, two: 1 }
#   if bytes([mp[o] for o in seq]) in ab: return True
#   return False
 


# for m in range(1, 10000):
#  lmbda = carmichael_lambda(m)
#  if lmbda % 12 != 0: continue
#  step = lmbda // 12
#  for _b in range(2, m):
#   b_cand = pow(_b,step,m)
#   if len(set([pow(b_cand, i, m) for i in range(12)])) == 12:
#     break
#  else:
#   print("!!!")
#   break
 
#  for b in [b_cand, pow(b_cand, 5, m)]:
#   if pow(b, 11, m) < b:
#     b = pow(b, 11, m)
#   orbit = [pow(b, i, m) for i in range(12)]

#   for m2 in [3,5,6,7]:
#     masked = [o%m2 for o in orbit]
#     if check_seq(masked):
#       print(f"{b}**i%{m}%{m2}: {masked}")
#   for i in range(m.bit_length()):
#     for j in range(i+1, m.bit_length()):
#       mask = (1<<i)|(1<<j)
#       masked = [o&mask for o in orbit]
#       if check_seq(masked):
#         print(f"{b}**i%{m}&{mask}: {masked}")



