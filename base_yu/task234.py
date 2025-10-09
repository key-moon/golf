# best: 115(biz) / others: 116(jacekw Potatoman nauti natte), 116(blob2822), 118(jailctf merger), 120(4atj sisyphus luke Seek mukundan), 120(ox jam)
# ====================================================== 115 ======================================================
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
