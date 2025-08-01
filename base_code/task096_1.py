def p(g):
 m,n=len(g),len(g[0])
 for k in range(m,0,-1):
  if k&1:
   for i in range(m-k+1):
    for j in range(n-k+1):
      s=[r[j:j+k]for r in g[i:i+k]]
      if len({*sum(s,[])})>1 and s==[t[::-1]for t in s]and s==s[::-1]:
        return s
 return g
