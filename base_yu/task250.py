# best: 117(jacekw Potatoman nauti natte) / others: 118(natte), 118(jailctf merger), 118(intgrah jimboko awu macaque sammyuri), 121(4atj sisyphus luke Seek mukundan), 121(ox jam)
# ======================================================= 117 =======================================================
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
