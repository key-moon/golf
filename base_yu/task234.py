# best: 109(biz) / others: 111(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 114(Krige), 114(import itertools), 116(jacekw Potatoman nauti natte), 116(blob2822)
# =================================================== 109 ===================================================
def p(g):
 for _ in 0,1:
  b=any(t>s and{*t}=={*s}>{0}for s,t in zip(g,g[1:]))
  u=[s for s in g if s.count(max(s))!=1]
  *g,=zip(*(u*b+u[:1]*(len(g)-len(u))+u*(1-b)))
 return g


# def p(g):
#  for _ in 0,1:
#   h=len(g)
#   b=any(g[i+1]>g[i]and{*g[i+1]}=={*g[i]}>{0}for i in range(h-1))
#   *g,=filter(lambda s:s.count(max(s))!=1,g)
#   g=g*b+[g[0]]*(h-len(g))+g*(1-b)
#   *g,=map(list,zip(*g))
#  return g
