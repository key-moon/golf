def p(g):
 q=range
 n=len(g)
 t=[[g[j][i]for j in q(n)]for i in q(n)]
 u=[r[::-1]for r in t]
 v=t[::-1]
 x=[r[::-1]for r in g[::-1]]
 return[g[i]+u[i]for i in q(n)]+[v[i]+x[i]for i in q(n)]