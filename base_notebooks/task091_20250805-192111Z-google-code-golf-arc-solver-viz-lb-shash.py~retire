def p(g,r=range):
 z=[a[:]for a in g];n,m=len(g),len(g[0])
 for i in r(n):
  for j in r(m):
   if g[i][j]==8and((i and g[i-1][j]==5)or(i<n-1and g[i+1][j]==5)):z[i][j]=5
 T=[j for i in r(n)if 5 in z[i]for j in r(m)if g[i][j]==5]
 return[g[i][min(T):max(T)+1]for i in r(n)if 5 in z[i]]