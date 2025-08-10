#eval(__import__("re").sub("[1-9]","1",str(g)))
#(0if v==0else 1for v in g[0],)

# p=lambda g:[[hash((*(bool(v)*2164 for v in g[0]),))%7]]
p=lambda g:[[hash((*((not v)*2164 for v in g[0]),))%7]]

# for mod in range(7, 30):
#   for repl in range(1, 10000):
#     for k, v in ({(1,1,0):1,(1,0,1):2,(0,1,1):3,(0,1,0):6}).items():
#       k = eval(str(k).replace("1",str(repl)))
#       if hash(k)%mod != 0:break
#     else:
#       print(f"{mod=} {repl=}")
