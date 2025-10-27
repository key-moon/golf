# best: 104(intgrah jimboko awu macaque sammyuri) / others: 111(HIMAGINE THE FUTURE.), 114(jailctf merger), 116(import itertools), 117(jacekw Potatoman nauti natte), 118(natte)
# ================================================ 104 =================================================
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
