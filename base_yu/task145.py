# best: 187(import itertools) / others: 189(intgrah jimboko awu macaque sammyuri), 191(Code Golf International), 191(4atj sisyphus luke Seek mukundan), 191(ox jam), 195(jailctf merger)
# ========================================================================================== 187 ==========================================================================================
def p(g):
 h,w=len(g),len(g[0])
#  u=sorted((x,i,j,r,d)for I in range(h*w)if((i:=I%h)<1 or g[i-1][j])if((j:=I//h)<1 or g[i][j-1])if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*[*zip(*g)][j][i:],2].index(2))))
#  u=sorted((x,i,j,r,d)for I in range(h*w)if((i:=I%h)<1 or g[i-1][j])if[1,*g[i]][j:=I//h]if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*[*zip(*g)][j][i:],2].index(2))))
 u=sorted((x,i,j,r,d)for I in range(h*w)if[[1]*w,*g][i:=I%h][j:=I//h]if[1,*g[i]][j]if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*[*zip(*g)][j][i:],2].index(2))))
 for x,i,j,d,r in u:
  for s in g[i:i+r]:
   s[j:j+d]=[(x==u[0][0])*8+(x==u[-1][0])]*d
 return g

# def p(g):
#  h,w=len(g),len(g[0])
#  u=sorted((x,i,j,r,d)for I in range(h*w)if((i:=I%h)<1 or g[i-1][j])if((j:=I//h)<1 or g[i][j-1])if(x:=((r:=[*g[i],2].index(2,j))-j)*((d:=[*(g[k][j]for k in range(h)),2].index(2,i))-i)))
#  for x,i,j,d,r in u:
#   for s in g[i:r]:
#    if x==u[0][0]:s[j:d]=[8]*(d-j)
#    if x==u[-1][0]:s[j:d]=[1]*(d-j)
#  return g

# def p(g):
#  h,w=len(g),len(g[0])
#  u=sorted((x,i,j,r,d)for I in range(h*w)if((i:=I%h)<1 or g[i-1][j])if((j:=I//h)<1 or g[i][j-1])if(x:=((r:=[*g[i],2].index(2,j))-j)*((d:=[*(k for k in range(i,h)if g[k][j]),h][0])-i)))
#  for x,i,j,d,r in u:
#   for s in g[i:r]:
#    if x==u[0][0]:s[j:d]=[8]*(d-j)
#    if x==u[-1][0]:s[j:d]=[1]*(d-j)
#  return g

# def p(g):
#  h,w=len(g),len(g[0])
#  u=sorted((x,i,j,r,d) for I in range(h*w) if ((i:=I%h)==0 or g[i-1][j]==2) and ((j:=I//h)==0 or g[i][j-1]==2) and (x:=((r:=[*g[i],2].index(2,j))-j)*((d:=[*(k for k in range(i,h)if g[k][j]),h][0])-i)))
#  for x,i,j,d,r in u:
#   for s in g[i:r]:
#    if x==u[0][0]:s[j:d]=[8]*(d-j)
#    if x==u[-1][0]:s[j:d]=[1]*(d-j)
#  return g

# def p(g):
#  h,w=len(g),len(g[0])
#  u=[]
#  for i in range(h):
#   for j in range(w):
#    if (i==0 or g[i-1][j]==2) and (j==0 or g[i][j-1]==2):
#     d=[*(k for k in range(i,h)if g[k][j]),h][0]
#     r=[*g[i],2].index(2,j)
#     u+=[((r-j)*(d-i),i,j,r,d)]
#  u = [(v,i,j,d,r) for v,i,j,d,r in u if v > 0]
#  u.sort()
#  for x,i,j,d,r in u:
#   for k in range(i,r):
#    if x==u[0][0]:
#     g[k][j:d]=[8]*(d-j)
#    if x==u[-1][0]:
#     g[k][j:d]=[1]*(d-j)
#  return g
