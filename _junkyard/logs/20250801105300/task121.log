def p(g):
 for r in range(1,len(g)-1):
  for c in range(1,len(g)-1):
   v=g[r-1][c]
   if v==g[r+1][c]==g[r][c-1]==g[r][c+1]!=g[r][c]:
    g[r][c]=v
    return[[g[x][y]for y in c-1,c,c+1]for x in r-1,r,r+1]