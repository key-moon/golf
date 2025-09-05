# best: 100(mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 122(xsot ovs att joking mewheni), 129(biz), 147(jacekwl), 147(jacekw), 162(MasukenSamba)
# ============================================== 100 ===============================================

# def p(g):
#  for _ in 0,1:
#   for i in range(15):
#    if g[i].count(2)>4:
#     # g[i-3:i+4]=[g[i+k-4]for k in(7,6,3,4,5,2,1)]
#     g[i-3:i+4]=[g[i+k-4]for k in b""]
#   *g,=zip(*g)
#  return g

p=lambda g,c=-29,k=3:c*g or exec("g[i-k],g[i+k]=g[i+k],g[i-k];k=2;"*2*(g[i:=c%15].count(2)>4))or p([*zip(*g)],c+1)

# def p(g):
#  for _ in 0,1:
#   for i in range(15):
#    if g[i].count(2)>4:g[i+2],g[i-2],g[i+3],g[i-3]=g[i-2],g[i+2],g[i-3],g[i+3]
#   *g,=zip(*g)
#  return g


# def p(g):
#  for _ in 0,1:
#   for i in range(15):
#    if g[i].count(2)>4:
#     g[i+2],g[i-2]=g[i-2],g[i+2]
#     g[i+3],g[i-3]=g[i-3],g[i+3]
#   *g,=zip(*g)
#  return[*map(list,g)]
