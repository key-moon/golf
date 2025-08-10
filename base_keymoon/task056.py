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
# 45
p=lambda g:[[hash((1300,*map(bool,g[1])))%7]]

# a = {
#   1:[[1,1,0],[1,0,1],[0,1,0]],
#   2:[[1,0,1],[0,1,0],[1,0,1]],
#   3:[[0,1,1],[0,1,1],[1,0,0]],
#   6:[[0,1,0],[1,1,1],[0,1,0]]
# }
# for mod in range(7, 30):
#   for mul in range(1, 10000):
#     ks = [k for k, v in a.items()]
#     vs = [hash((mul,*map(bool,v[2]))) % mod for k, v in a.items()]
#     # print(ks, vs)
#     if ks == vs:
#       print(f"{mod=} {mul=}")
#       pass
