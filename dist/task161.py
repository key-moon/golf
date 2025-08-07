R=range
def p(g):
 h,w=len(g),len(g[0])
 s=sum([s[1:w-1]for s in g[1:h-1]],[])
 u=[w*[(g[i][0]not in s)*g[i][0]]for i in R(h)]
 for I in R(w*h):
  if g[0][I%w]not in s:u[I//w][I%w]=g[0][I%w]
 return u