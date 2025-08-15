def p(g):
 G=[*filter(bool,[*filter(any,g)][2])]
 c=G[len(G)//2]
 for _ in range(4):
  I=[[*g[i],c].index(c) for i in range(21)]
  i=[i for i in range(21)if I[i]<21][0]
  j=min(I[i] for i in range(21)if I[i]<21)
  d=max(g[i+4][j:j+3])
  e=max(g[i+4][j+3:])
  if CASE==71:
   print(c,I,i,j,d,e)
  for k in range(i+4,21):
   g[k][j:j+3]=[v and d for v in g[k-4][j:j+3]]
   l=j+(k-i)//4*4
   for x in range(3):
    if l+x<21:
     g[k][l+x]=g[k-4][l-4+x] and e
  *g,=map(list,zip(*g[::-1]))
 return g
