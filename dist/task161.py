B=range
def p(g):
 h,w=len(g),len(g[0]);s=sum([s[1:w-1]for s in g[1:h-1]],[]);u=[w*[(g[i][0]not in s)*g[i][0]]for i in B(h)]
 for A in B(w*h):
  if g[0][A%w]not in s:u[A//w][A%w]=g[0][A%w]
 return u