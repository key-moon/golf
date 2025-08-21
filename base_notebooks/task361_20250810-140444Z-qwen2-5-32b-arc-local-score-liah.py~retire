R=range;E=enumerate
def A(p,x,y,t):
 for i in R(x,x+t):
  for j in R(y,y+t):
   if i<len(p)and  j<len(p[0]):
    if p[i][j]==0:return 0
 return 1
def B(p):
 h,w=len(p),len(p[0])
 for k in R(w-2,1,-1):
  for i in R(0,h-k):
   for j in R(0,w-k):
    if A(p,i,j,k):return(i,j,k)
 return-1
def N(p):
 n=0
 for r in p:
  for c in r:
   if c:n+=1
 return n
def G(p,m,n,k,t):
 a=0
 for i in R(m-t,m+k+t):
  for j in R(n-t,n+k+t):
   if p[i][j]:a+=1
 return a
def C(p):
 i,j,k=B(p)
 n=N(p)
 t=1
 while 1:
  if n==G(p,i,j,k,t):return k+2*t,i-t,j-t
  t+=1
def D(g):
 h,w=len(g),len(g[0])
 p=[i[:]for i in g]
 for r,s in E(g):
  for c,d in E(s):
   if p[c][w-1-r]==0:p[c][w-1-r]=g[r][c]
 return p
def p(g):
 k,x,y=C(g)
 a=[[0]*k for _ in R(k)]
 for i in R(x,x+k):
  for j in R(y,y+k):a[i-x][j-y]=g[i][j]
 a=D(D(D(a)))
 b=[i[:]for i in g]
 for i in R(x,x+k):
  for j in R(y,y+k):b[i][j]=a[i-x][j-y]
 return b