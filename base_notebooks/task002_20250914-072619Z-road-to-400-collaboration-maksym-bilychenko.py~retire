def p(g):
 def f(i,j):
  try:
   if g[i][j]<1:g[i][j]=1;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
  except:0
 for i in range(len(g)):f(i,0);f(i,-1);f(0,i);f(-1,i)
 return[[(4,0,0,3)[a]for a in r]for r in g]