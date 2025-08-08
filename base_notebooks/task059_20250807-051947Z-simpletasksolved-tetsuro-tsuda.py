def p(g):
 q=range
 r=[o[:]for o in g]
 p=[(0,0),(0,4),(0,8),(4,0),(4,4),(4,8),(8,0),(8,4),(8,8)]
 c=[]
 for i,j in p:
  d={}
  for x in q(3):
   for y in q(3):
    v=g[i+x][j+y]
    if v and v!=5:d[v]=d.get(v,0)+1
  c.append((max(d.values())if d else 0,list(d.keys())[0]if d else 0,i,j))
 m=max(c[0]for c in c)
 for k,l,i,j in c:
  for x in q(3):
   for y in q(3):
    r[i+x][j+y]=l if (k==m)&(k>0)else 0
 return r