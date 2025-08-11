def p(g,k=range):
 h,w=len(g),len(g[0])
 s=[0 for _ in k(w)]
 for i in k(w):
  for j in k(h):
   if g[j][i]>0:s[i]+=1
   g[j][i]=0
 m=min([c for c in s if c>0])
 i=s.index(m)
 for j in k(s[i]):g[-(j+1)][i]=2
 i=s.index(max(s))
 for j in k(s[i]):g[-(j+1)][i]=1
 return g