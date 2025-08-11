def p(g):
 q=range
 n=(len(g)-1)//2
 if n==1:
  b=[g[0][0],g[0][2],g[2][0],g[2][2]]
  for v in b:
   if b.count(v)==1:return[[v]]
 for o,r in[(0,0),(0,n+1),(n+1,0),(n+1,n+1)]:
  s=[[g[o+i][r+j]for j in q(n)]for i in q(n)]
  v=[s[i][j]for i in q(n)for j in q(n)]
  if len(set(v))>1:return s
