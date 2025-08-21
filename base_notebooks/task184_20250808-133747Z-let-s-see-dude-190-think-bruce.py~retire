def p(g,w=len):
 R=range
 n,m=w(g),w(g[0])
 r=[i for i in R(n)if all(g[i][j]==0for j in R(m))]
 c=[j for j in R(m)if all(g[i][j]==0for i in R(n))]
 r=[-1]+r+[n]
 c=[-1]+c+[m]
 o=[]
 for i in R(w(r)-1):
  t=[]
  for j in R(w(c)-1):
   for x in R(r[i]+1,r[i+1]):
    for y in R(c[j]+1,c[j+1]):
     if g[x][y]:t.append(g[x][y]);break
    else:continue
    break
  if t:o.append(t)
 return o