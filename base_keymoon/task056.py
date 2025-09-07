# best: 40(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni, mukundan) / others: 42(4atj sisyphus luke Seek), 42(intgrah jimboko awu macaque sammyuri), 44(HETHAT), 49(dbdr), 50(natte)
# ================= 40 =================
# 53
# p=lambda g:[[hash((*((1>v)*2164 for v in g[0]),))%7]]
# for mod in range(7, 30):
#   for repl in range(1, 10000):
#     for k, v in ({(1,1,0):1,(1,0,1):2,(0,1,1):3,(0,1,0):6}).items():
#       k = eval(str(k).replace("1",str(repl)))
#       if hash(k)%mod != 0:break
#     else:
#       print(f"{mod=} {repl=}")

# a = {
# 1:[[1,1,0],[1,0,1],[0,1,0]],
# 2:[[1,0,1],[0,1,0],[1,0,1]],
# 3:[[0,1,1],[0,1,1],[1,0,0]],
# 6:[[0,1,0],[1,1,1],[0,1,0]]
# }

# sum(g[2])*2+

# {(0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 0), (0, 1, 0, 0), (0, 1, 1, 0), (1, 0, 0, 1)}
# print(set([(*(v[i][j] for v in a.values()),) for i in range(3) for j in range(3)]))

# (1,0): 1, 1*1
# (1,1): 2, 2*1
# (0,1): 3, 1*3
# (0,0): 6, 2*3

# 54
# p=lambda g:[[(1+2*(1>(a:=g[0][0])))*(1+(a==g[0][2]))]]

# 49
# p=lambda g:[[hash((2174,0<g[0][0],0<g[0][2]))%7]]
# p=lambda g:[[hash((288,1>g[0][0],0<g[0][2]))%12]]
# p=lambda g:[[b"1236"[(1>g[0][0])*2+(1>g[0][2])]]]
# 48
# p=lambda g:[[b"????"[str(g)[10::2].count("0")]]]
# 45
p=lambda g:[[hash((1300,*map(bool,g[1])))%7]]

# str(g)[4::2]
# {1: 4, 2: 0, 3: 1, 6: 3}
# {1: 4, 2: 0, 3: 1, 6: 3}
# {1: 4, 2: 0, 3: 1, 6: 3}
# str(g)[10::2]
# str(g)[12::2]
# str(g)[14::2]
# str(g)[16::2]
# {1: 3, 2: 0, 3: 1, 6: 2}

# a = { 
#   1:[[1,1,0],[1,0,1],[0,1,0]],
#   2:[[1,0,1],[0,1,0],[1,0,1]],
#   3:[[0,1,1],[0,1,1],[1,0,0]],
#   6:[[0,1,0],[1,1,1],[0,1,0]]
# }
# for start in range(len(str(a[1]))):
#   for stride in range(1,len(str(a[1]))):
#     s = set([str(v)[start::stride].count("0") for k, v in a.items()])
#     if len(s) != 4:
#       continue
#     print(f"str(g)[{start}::{stride}]")
#     print({k:str(v)[start::stride].count("0") for k, v in a.items()})
#     for mod in range(7, 12):
#       for mul in range(-1000, 10000):
#         ks = [k for k, v in a.items()]
#         vs = [str(v)[start::stride].count("0")*mul % mod for k, v in a.items()]
#         if ks == vs:
#           print(f"{mod=} {mul=}")
#           break



# for i in 0,1:
#   for mod in range(7, 12):
#     for mul in range(-1000, 10000):
#       ks = [k for k, v in a.items()]
#       vs = [hash((mul,*map(bool,v[i]))) % mod for k, v in a.items()]
#       # print(ks, vs)
#       if ks == vs:
#         print(f"{mod=} {mul=} {i=}")
#         break
