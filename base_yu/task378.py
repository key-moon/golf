R=range
def p(g):
 n,u=len(g),[]
 for i in R(1,n-1):
  for j in R(1,n-1):
   s=[g[i+k%3-1][j+k//3-1]for k in R(9)]
   *t,={*s}-{*s[1::2]}
   u+=[(j+(1-(2&(k:=-~s.index(t[0])//3)))*m,i+(1-k%2*2)*m,*t)for m in R(2,n*(len(t)*3==len({*s})))]
 for x,y,v in u:
  if y in R(n)and x in R(n):g[y][x]=v
 return g


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
