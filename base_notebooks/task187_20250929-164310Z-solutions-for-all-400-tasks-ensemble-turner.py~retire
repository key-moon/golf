def p(H):
 l,e,E=len(H),len(H[0]),range;d=[(i,o)for i in(0,l-1)for o in E(e)if H[i][o]<1]+[(i,o)for i in E(l)for o in(0,e-1)if H[i][o]<1]
 while d:
  i,o=d.pop()
  if H[i][o]<1:H[i][o]=3;d+=[(i,o)for(i,o)in((i+1,o),(i-1,o),(i,o+1),(i,o-1))if 0<=i<l and 0<=o<e and H[i][o]<1]
 for i in E(l):
  for o in E(e):
   if H[i][o]<1:H[i][o]=2
 return H