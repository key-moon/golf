# best: 127(xsot ovs att joking mewheni, jailctf merger) / others: 131(4atj sisyphus luke Seek), 143(mukundan), 161(MasukenSamba), 200(natte), 202(kdmitrie)
# ============================================================ 127 ============================================================
p=lambda g,c=-3:c*g or p([*zip(*([[0]*10]*~-(i:=str(g).index("2")//31)+[[*map(max,*g[:i])]]+g[i:])[::-1])],c+1)

# def p(g):
#  for _ in range(4):
# #   i=0;while 1-(2in g[i]):i+=1
# #   i=[i for i in range(10)if 2in g[i]][0]
# #   i=g.index([s for s in g if 2in s][0])
# #   i=g.index(max(g,key=lambda s:2in s))
#   i=str(g).index("2")//31
#   g=[[0]*10]*~-i+[[*map(max,*g[:i])]]+g[i:]
#   g=[*zip(*g[::-1])]
#  return g
