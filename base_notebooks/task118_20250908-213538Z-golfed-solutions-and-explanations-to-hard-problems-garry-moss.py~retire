# def p(g,L=2):E=range;H=len(g);W=len(g[0]);R={(r,c)for r in E(H)for c in E(W)if g[r][c]&2};S=lambda Q,U:[Q and(S(Q[1:],U)or{1}>Q[0]&U and S(Q[1:],U|Q[0])),U][R<=U];return(U:=S([C for r in E(H)for c in E(W)for C in[{(y,x)for k in E(-L,L+1)for y,x in[(r+k,c),(r,c+k)]if H>y>-1<x<W}]if min(g[y][x]for y,x in C)&2],set()))and(exec('for r,c in U:g[r][c]+=3*(g[r][c]&1)')or g)or p(g,3)

def p(p):
 t={(l,n)for l in range(len(p))for n in range(len(p[0]))if p[l][n]&2};d=lambda i,l:[i and(d(i[1:],l)or not i[0]&l and d(i[1:],l|i[0])),l][t<=l]
 for n in 2,3:
  l=[l for d in range(len(p))for i in range(len(p[0]))for l in[{(l,n)for l in range(-n,n+1)for l,n in[(d+l,i),(d,i+l)]if len(p)>l>-1<n<len(p[0])}]if min(p[l][n]for l,n in l)&2]
  if l:=d(l,set()):
   for l,n in l:p[l][n]+=3*(p[l][n]&1)
   return p