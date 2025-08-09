def p(g):
 G=sum(g,t:=[])
 F,*C=sorted((G.count(v),v)for v in{*G})
 for _,c in C:
  l,*_,r=sorted(j for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c)
  u,*_,d=sorted(i for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c)
  t+=[(sum(s[l:r+1].count(F[1])for s in g[u:d+1]),c)]
 return [[max(t)[1]]]


# def p(g):
#  G=sum(g,t:=[])
#  F,*C=sorted((G.count(v),v)for v in{*G})
#  h,w=len(g),len(g[0])
#  for _,c in C:
#   l,*_,r=sorted(i%w for i in range(h*w)if g[i//w][i%w]==c)
#   u,*_,d=sorted(i//w for i in range(h*w)if g[i//w][i%w]==c)
#   t+=[(sum(s[l:r+1].count(F[1])for s in g[u:d+1]),c)]
#  return [[max(t)[1]]]

# def p(g):
#  G=sum(g,t:=[])
#  F,*C=sorted((G.count(v),v)for v in{*G})
#  h,w=len(g),len(g[0])
#  for _,c in C:
#   x=[i for i in range(h*w)if g[i//w][i%w]==c]
#   l,*_,r=sorted(i%w for i in x)
#   u,*_,d=sorted(i//w for i in x)
#   t+=[(sum(s[l:r+1].count(F[1])for s in g[u:d+1]),c)]
#  return[[max(t)[1]]]
