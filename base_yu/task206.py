# best: 144(jailctf merger) / others: 151(jonas ryno kg583 kabutack), 151(jonas ryno kg583), 154(JRK), 156(ox jam), 156(xsot ovs att joking mewheni)
# ==================================================================== 144 =====================================================================

def p(g):
 y,x=divmod(sum(g,[]).index(5),len(g[0]))
 g[y][x]=k=0
 for v in[v for s in g for*t,v in zip(*g,s)if any(s)*any(t)]:
  g[y-1+k//3][x-1+k%3]=v
  k+=1
 return g

# def p(g):
#  y,x=divmod(sum(g,[]).index(5),len(g[0]))
#  g[y][x]=0
#  u=g.index(max(g,key=any))
#  v=max(g).index(max(max(g),key=bool))
#  for k in 0,1,2:
#   g[y-1+k][x-1:x+2]=g[u+k][v:v+3]
#  return g
