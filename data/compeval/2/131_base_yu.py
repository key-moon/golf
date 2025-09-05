# best: 126(xsot ovs att joking mewheni) / others: 140(jailctf merger), 178(mukundan), 225(jacekwl), 257(Potatoman), 257(MasukenSamba)
# =========================================================== 126 ============================================================

# p=lambda g,c=-3:c*g or p([*zip(*(2in(f:=[*map(max,g)])and(k:=f.index(2))>f.index(3)and sorted([[8]*len(g[0])]+g[:k],key=any)[1:]+g[k:]or g)[::-1])],c+1)
p=lambda g,c=-3:c*g or p([*zip(*(g*(2in max(g,key=any))or sorted([[8]*len(g[0])]+g[:(k:=[*map(max,g)].index(2))],key=any)[1:]+g[k:])[::-1])],c+1)

# def p(g):
#  for i in range(4):
#   if 2 not in max(g,key=any):
#    k=[*map(max,g)].index(2)
#    g=sorted([[8]*len(g[0])]+g[:k],key=any)[1:]+g[k:]
#   g=[*zip(*g[::-1])]
#  return g