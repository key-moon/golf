# def p(g):a=g[0];d={i:v for i,v in enumerate(a)if v};m=len(a)*len(d);return[[d.get(r+j-m+1,0)for j in range(m)]for r in range(m)]

# def p(g):
#  m=5*sum(map(bool,g[0]))
#  a=[0]*~-m+g[0]
# #  a=[0]*~-m+g[0]+[0]*m
#  return [(a[i:]+[0]*i)[:m] for i in range(m)]

# p=lambda g:(m:=5*sum(map(bool,a:=g[0])))and[([0]*(m-1-i)+a+[0]*m)[:m]for i in range(m)]

def p(g):
 m=5*sum(map(bool,a:=g[0]))
 return[([0]*(m-1-i)+a+[0]*m)[:m]for i in range(m)]

# def p(g):
#  m=5*sum(map(bool,a:=g[0]))
#  return[([0]*(m-1-i)+a+[0]*m)[:m]for i in range(m)]

# def p(g):
#  m=5*sum(map(bool,a:=g[0]))
#  return[([0]*(m-1-i)+a+[0]*m)[:m]for i in range(m)]

#  b=[(v,i)for i,v in enumerate(a)if v]
#  m=len(a)*len(b)
#  g=[[0]*m for _ in range(m)]
#  for s in range(m):
#   for v,i in b:
#    k=i+s
#    if k<m:g[m-1-s][k]=v
