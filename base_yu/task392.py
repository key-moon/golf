# def p(g):
#  d=lambda i,j,k:max(abs(j*2+1-i//21),abs(k*2+1-i%21))
#  b,v=0,9
#  for i in range(441):
#   m={(d(i,j//10,j%10),g[j%10][j//10])for j in range(100)}
#   if len(m)==len(m:=dict(m)) and v>(k:=sum(map(bool,m.values()))):
#    v,b,u=k,i,m
#  x,y,*_=sorted(k for k,v in u.items()if v)
#  return[[u[d(b,j,i)%(y-x)]or 5for j in range(10)]for i in range(10)]

# def p(g):
#  d=lambda i,j:max(abs(j//10*2+1-i//21),abs(j%10*2+1-i%21))
#  b,v=0,9
#  for i in range(441):
#   m={(d(i,j),g[j%10][j//10])for j in range(100)}
#   if v>(k:=sum(v>0for _,v in m))and len(m)==len(m:=dict(m)):
#    v,b,u=k,i,m
#  x,y,*_=sorted(k for k,v in u.items()if v)
# #  return[[u[d(b,j*10+i)%(y-x)]or 5for j in range(10)]for i in range(10)]
#  for i in range(100):
#   g[i%10][i//10]=u[d(b,i)%(y-x)]or 5
#  return g

def p(g):
 d=lambda i,j:max(abs(j//10*2+1-i//21),abs(j%10*2+1-i%21))
 b,v=0,9
 for i in range(441):
  m={(d(i,j),g[j%10][j//10])for j in range(100)}
  if v>(k:=sum(v>0for _,v in m))and len(dict(m))==len(u:=m):v,b=k,i
 x,y,*_=sorted(k for k,v in u if v)
#  return[[u[d(b,j*10+i)%(y-x)]or 5for j in range(10)]for i in range(10)]
 for i in range(100):g[i%10][i//10]=dict(u)[d(b,i)%(y-x)]or 5
 return g

# def p(g):
#  d=lambda i,j:max(abs(j//10*2+1-i//21),abs(j%10*2+1-i%21))
#  b,v=0,9
#  for i in range(441):
#   m={(d(i,j),g[j%10][j//10])for j in range(100)}
#   if len(m)==len(m:=dict(m))and v>(k:=sum(map(bool,m.values()))):
#    v,b,u=k,i,m
#  x,y,*_=sorted(k for k,v in u.items()if v)
# #  return[[u[d(b,j*10+i)%(y-x)]or 5for j in range(10)]for i in range(10)]
#  for i in range(100):
#   g[i%10][i//10]=u[d(b,i)%(y-x)]or 5
#  return g
