# best: 82(luke, 4atj sisyphus luke Seek, 4atj, luke/sisyphus/Seek, biz, sisyphus) / others: 84(HashPanda), 87(natte), 90(mukundan), 93(kg583), 93(kabutack)
# ====================================== 82 ======================================

# p=lambda g:[[max((t[0]&t[-1]),(s[0]&s[-1])) for t in zip(*g)]for s in g]
# p=lambda g:(c:=min((u:=sum(g,[])),key=u.count))and[[c*([t[0],s[0]].count(c)>0) for t in zip(*g)]for s in g]
# p=lambda g:(c:=min((u:=sum(g,[])),key=u.count))and[[c*(c in[t[0],s[0]])for t in zip(*g)]for s in g]
p=lambda g:[[sum({min((u:=sum(g,[])),key=u.count)}&{t[0],s[0]})for t in zip(*g)]for s in g]

# R=range
# def p(g):
#  h,w=len(g),len(g[0])
#  s=sum([s[1:w-1]for s in g[1:h-1]],[])
#  u=[w*[(g[i][0]not in s)*g[i][0]]for i in R(h)]
#  for I in R(w*h):
#   if g[0][I%w]not in s:u[I//w][I%w]=g[0][I%w]
#  return u
  

# R=range
# def p(g):
#  h,w=len(g),len(g[0])
#  _,c=max((sum(.5-(0<i<h-1 and 0<j<w-1) for j in R(w)for i in R(h)if g[i][j]==c),c)for c in R(1,10))
#  u=[w*[(g[i][0]==c)*c]for i in R(h)]
#  for i in R(w):
#   for j in R(h*(g[0][i]==c)):u[j][i]=c
#  return u

# def p(g):
#  h,w=len(g),len(g[0])
#  _,c=max((sum(.5-(0<i<h-1 and 0<j<w-1) for j in range(w) for i in range(h) if g[i][j]==c),c) for c in range(1,10))
#  u=[[[0,c][g[i][0]==c]]*w for i in range(h)]
#  for i in range(w):
#   if g[0][i]==c:
#    for j in range(h):
#     u[j][i]=c
#  return u