# best: 81(jailctf merger) / others: 85(4atj sisyphus luke Seek mukundan), 85(Code Golf International), 86(intgrah jimboko awu macaque sammyuri), 87(biz), 91(import itertools)
# ====================================== 81 =====================================
# p=lambda g,c=-1:c*g or p([[([0,*s,0][i:i+3:2]>[0,0])*s[i] for i in range(len(s))]for s in zip(*g)],c+1)
# p=lambda g,c=-1:c*g or p([[any([0,*s][i:i+3:2])*s[i]for i in range(len(s))]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or[[v*any([0,*s][i:i+3:2])for i,v in enumerate(s)]for s in zip(*p(g,c+1))]
# p=lambda g,R=range:(n:=len(g))and[[sum(-1<(y:=i+abs(k-2)-1)<n>(x:=j+abs(k-1)-1)>-1and g[y][x]>0for k in R(4))>1and g[i][j]for j in R(n)]for i in R(n)]

# import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub('(0, |\()[^0](, 0|\))',r'\1 0\2',str(p(g,c+1)))))]

# R=range
# p=lambda g:(n:=len(g))and[[sum(-1<(y:=i+abs(k-2)-1)<n and-1<(x:=j+abs(k-1)-1)<n and g[y][x]>0for k in R(4))>1and g[i][j] or 0for j in R(n)]for i in R(n)]

# p=lambda g:(n:=len(g))and[[sum(-1<(y:=i+abs(k-2)-1)<n and-1<(x:=j+abs(k-1)-1)<n and g[y][x]>0for k in range(4))>1and g[i][j] or 0for j in range(n)]for i in range(n)]

# def p(g):
#  n=len(g)
#  for i in range(n):
#   for j in range(n):
#    if sum(-1<(y:=i+abs(k-2)-1)<n and-1<(x:=j+abs(k-1)-1)<n and g[y][x]>0 for k in range(4)) < 2:
#     g[i][j]=0
#  return g

# def p(g):
#  n=len(g)
#  for i in range(n):
#   for j in range(n):
#    c = 0
#    for k in range(4):
#     y=i+abs(k-2)-1
#     x=j+abs(k-1)-1
#     if-1<y<n and-1<x<n and g[y][x]:
#      c += 1
#    if c < 2:
#     g[i][j]=0
#  return g
