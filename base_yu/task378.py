# best: 143(jailctf merger) / others: 144(xsot ovs att joking mewheni), 145(natte), 145(4atj sisyphus luke Seek mukundan), 228(MasukenSamba), 265(Yuchen20)
# ==================================================================== 143 ====================================================================
import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=(.{%d}.{4})*.{%d}0, ([1-9]), \2.{%d}.{%d}.0, ([1-9]))"%((len(g)*3+1,)*4),r"\3",str(p(g,c+1))))[::-1])]


# import re
# def p(g):
#  for _ in range(4):
#   x=len(g)*3+5
#   y=len(g)*3+1
#   z=len(g)*6+3
#   g=[*zip(*eval(re.sub(r"0(?=(.{%d})*.{%d}0, ([1-9]), \2.{%d}0, ([1-9]))"%(x,y,z),r"\3",str(g)))[::-1])]
#  return g

# R=range
# def p(g):
#  n,u=len(g),[]
#  for i in R(1,n-1):
#   for j in R(1,n-1):
#    s=[g[i+k%3-1][j+k//3-1]for k in R(9)]
#    *t,={*s}-{*s[1::2]}
#    u+=[(j+(1-(2&(k:=-~s.index(t[0])//3)))*m,i+(1-k%2*2)*m,*t)for m in R(2,n*(len(t)*3==len({*s})))]
#  for x,y,v in u:
#   # if y in R(n)and x in R(n):g[y][x]=v
#   if-1<y<n and-1<x<n:g[y][x]=v
#  return g


# R=range
# def p(g):
#  n=len(g)
#  u=[s[:] for s in g]
#  for i in R(1,n-1):
#   for j in R(1,n-1):
#    s=[g[i+k%3-1][j+k//3-1]for k in R(9)]
#    *t,={*s}-{*s[1::2]}
#    if len(t)*3==len({*s}):
#     k=-~s.index(t[0])//3
#     for m in R(2,n):
#      x=j+[1,1,-1,-1][k]*m
#      y=i+[1,-1,1,-1][k]*m
#      if y in R(n)and x in R(n):u[y][x]=t[0]
#  return u










