def p(g):
 for _ in range(4):
  while 1-all(g[0]):
   g=g[1:]
  *g,=map(list,zip(*g[::-1]))
 for _ in range(4):
  for s in g:
   for j in range(len(s)):
    if s[j]==s[0]:
     s[:j]=[s[0]]*j
  *g,=map(list,zip(*g[::-1]))
 return g
