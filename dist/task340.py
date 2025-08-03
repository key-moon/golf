def p(g):
 for _ in(u:=[0])*4:
  for s in g[1:-1]:
   if s[0]in s[1:]:s[s.index(s[0],1)],s[1]=0,s[0]
   u+=[s[0]]
  *g,=map(list,zip(*g[::-1]))
 for s in g:
  for j in range(len(s)):
   if s[j]not in u:s[j]=0
 return g