# best: 193(jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 195(xsot ovs att joking mewheni), 204(natte), 207(4atj sisyphus luke Seek mukundan), 221(kdmitrie), 221(Ali)
# ============================================================================================= 193 =============================================================================================

def p(g):
 u=v=w=0
 for i in range(21):
  for j in range(21):
#    if(t:=sum((g[i-y-1][j-x-1]==g[y][x]>0)-.9for x in R(10)for y in R(10)if max(abs(j-2*x-1),abs(i-2*y-1))<3if i-y-1 in R(10)if j-x-1 in R(10)))>w:u,v,w=i-j,i+j,t
#    if(t:=sum((g[c][d]==g[y][x]>0)-.9for x in R(10)for y in R(10)if max(abs((c:=i-y-1)-y),abs((d:=j-x-1)-x))<3if c in R(10)if d in R(10)))>w:u,v,w=i-j,i+j,t
   if(t:=sum((g[c][d]==g[y][x]>0)-.9for x in range(10)for y in range(10)if-1<(c:=i-y-1)<10if-1<(d:=j-x-1)<10if max(abs(c-y),abs(d-x))<3))>w:u,v,w=i-j,i+j,t
#    if(t:=sum((g[c][d]==g[y][x]>0)-.9for x in R(10)for y in R(10)if max(abs(c:=i-2*y-1),abs(d:=j-2*x-1))<3if c+y in R(10)if d+x in R(10)))>w:u,v,w=i-j,i+j,t
 for k in range(400):
  if g[y:=k%10][x:=k//10%10]>0:g[u//2+x][v//2-1-y]=g[y][x]
 return g


# R=range
# def p(g):
#  bi=bj=bv=0
#  for i in R(21):
#   for j in R(21):
#    ok=0
#    for y in R(10):
#     for x in R(10):
#      if max(abs(j-2*x-1),abs(i-2*y-1))<=2:
#       ok-=.9-(i-y-1 in R(10)and j-x-1 in R(10)and g[i-y-1][j-x-1]==g[y][x]>0)
#    if ok>bv:
#     bi,bj,bv=i,j,ok
#  for _ in R(4):
#   for y in R(10):
#    for x in R(10):
#     if g[y][x]>0:
#      g[(bi-bj)//2+x][(bj+bi)//2-1-y]=g[y][x]
#     #  g[(bi-bj+(x*2+1))//2][(bj+bi-(y*2+1))//2] = g[y][x]
#  return g

# def p(g,case):
#  bi=bj=bv=0
#  for i in range(21):
#   for j in range(21):
#    ok=0
#    for y in range(10):
#     for x in range(10):
#      if max(abs(j-2*x-1),abs(i-2*y-1))<=2:
#       ok-=.9-(i-y-1 in range(10)and j-x-1 in range(10)and g[i-y-1][j-x-1]==g[y][x]>0)
#    if ok>bv:
#     bi,bj,bv=i,j,ok
#  for _ in range(4):
#   for y in range(10):
#    for x in range(10):
#     if g[y][x]>0:
#      g[(bi-bj)//2+x][(bj+bi)//2-1-y]=g[y][x]
#     #  g[(bi-bj+(x*2+1))//2][(bj+bi-(y*2+1))//2] = g[y][x]
#  return g

# R=range
# def p(g):
#  d=lambda i,j:max(abs(j//10*2+1-i//21),abs(j%10*2+1-i%21))
#  b,v=0,9
#  for i in R(441):
#   m={(d(i,j),g[j%10][j//10])for j in R(100)}
#   if v>(k:=sum(v>0for _,v in m))and len(dict(m))==len(u:=m):v,b=k,i
#  x,y,*_=sorted(k for k,v in u if v)
# #  return[[u[d(b,j*10+i)%(y-x)]or 5for j in range(10)]for i in range(10)]
#  for i in R(100):g[i%10][i//10]=dict(u)[d(b,i)%(y-x)]or 5
#  return g
