def p(g):
 n,x,y=len(g),3-(g[0][0]==g[0][2]),3-(g[0][0]==g[2][0]);A=range(n)
 for i in A:
  s=g[i]=g[i][1:]+[g[i][-1]]
  for j in A:
   if s[j]==g[-1][-1]:s[j]=g[i%y][j%x]
 return g