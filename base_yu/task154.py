# best: 108(mukundan) / others: 110(4atj sisyphus luke Seek), 110(4atj), 133(joking), 133(joking MeWhenI), 198(MasukenSamba)
# ================================================== 108 ===================================================
p=lambda g,c=-29,k=3:c*g or exec("g[i-k],g[i+k]=g[i+k],g[i-k];k=2;"*2*(g[i:=c%15].count(2)>4))or p([*zip(*g)],c+1)

# def p(g):
#  for i in range(30):
#   i%=15
#   if g[i].count(2)>4:
#    k=3
#    exec("g[i-k],g[i+k]=g[i+k],g[i-k];k=2;"*2)
# #    g[i-3],g[i+3]=g[i+3],g[i-3]
# #    g[i-2],g[i+2]=g[i+2],g[i-2]
# #    g[i-3:i+4]=g[i-3:i+4][::-1]
# #    g[i-1:i+2]=g[i-1:i+2][::-1]
#   *g,=zip(*g)
#  return g

# def p(g):
#  for i in range(30):
#   i%=15
#   if g[i].count(2)>4:
#    g[i-3:i-1],g[i+2:i+4]=g[i+3:i+1:-1],g[i-3:i-1][::-1]
#   *g,=zip(*g)
#  return g
