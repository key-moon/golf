# best: 187(import itertools, jailctf merger) / others: 191(Code Golf International), 191(4atj sisyphus luke Seek mukundan), 191(ox jam), 214(biz), 215(THUNDER THUNDER)
# ========================================================================================== 187 ==========================================================================================
def p(g):
#  h,w=len(g),len(g[0]);u=sorted((x,i,j,r,d)for I in range(h*w)if[[1]*w,*g][i:=I%h][j:=I//h]if[1,*g[i]][j]if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*[*zip(*g)][j][i:],2].index(2))))
#  u=sorted((x,i,j,r,d)for i in range(len(g))for j in range(len(g[0]))if[[1]*99,*g][i][j]if[1,*g[i]][j]if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*[*zip(*g)][j][i:],2].index(2))))
#  u=sorted((x,i,j,r,d)for i in range(len(g))for j in range(len(g[0]))if(x:=(r:=(u:=[1,*g[i],2])[j+1:].index(2))*(d:=(v:=[1,*[*zip(*g)][j],2])[i+1:].index(2)))if u[j]if v[i])
#  u=sorted((x,i,j,r,d)for i in range(len(g))for j in range(len(g[0]))if(x:=(r:=[1,*g[i],2][j+1:].index(2))*(d:=[1,*[*zip(*g)][j],2][i+1:].index(2)))if [1,*g[i],2][j]if [1,*[*zip(*g)][j],2][i])
 u=sorted((r*d,i,j,r,d)for i in range(len(g))for j in range(len(g[0]))if(r:=[*g[i],2][j:].index(2))*(d:=[*[*zip(*g)][j],2][i:].index(2))if[1,*g[i]][j]if[1,*[*zip(*g)][j]][i])
#  u=sorted((x,i,j,r,d)for I in range(h*w)if((i:=I%h)<1 or g[i-1][j])if((j:=I//h)<1 or g[i][j-1])if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*[*zip(*g)][j][i:],2].index(2))))
#  u=sorted((x,i,j,r,d)for I in range(h*w)if((i:=I%h)<1 or g[i-1][j])if[1,*g[i]][j:=I//h]if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*[*zip(*g)][j][i:],2].index(2))))
 for x,i,j,d,r in u:
  for s in g[i:i+r]:
   s[j:j+d]=[(x==u[0][0])*8+(x==u[-1][0])]*d
 return g


# def p(g):
#  a=[]
#  a+=[(l:=0)or[l:=-~l*0**v for v in s]for s in g],
#  g[:]=zip(*g[::-1])
#  a+=[(l:=0)or[l:=-~l*0**v for v in s]for s in g],
#  g[:]=zip(*g[::-1])
#  a+=[(l:=0)or[l:=-~l*0**v for v in s]for s in g],
#  g[:]=zip(*g[::-1])
#  a+=[(l:=0)or[l:=-~l*0**v for v in s]for s in g],
#  g[:]=zip(*g[::-1])
#  b=sorted((a[0][i][j]+a[2][~i][~j]-1)*(a[1][j][~i]+a[3][~j][i]-1)for i in range(len(g))for j in range(len(g[i]))if g[i][j]<1)
#  return[[g[i][j]or(b[0]==(a[0][i][j]+a[2][~i][~j]-1)*(a[1][j][~i]+a[3][~j][i]-1))*8+(b[-1]==(a[0][i][j]+a[2][~i][~j]-1)*(a[1][j][~i]+a[3][~j][i]-1))for j in range(len(g[i]))]for i in range(len(g))]


#  return[[(a[0][i][j]+a[2][~i][~j])*(a[1][j][~i]+a[3][~j][i]) for j in range(len(g[i]))]for i in range(len(g))]

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
