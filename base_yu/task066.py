# best: 268(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 275(ox jam), 299(jacekw Potatoman nauti natte), 299(natte), 303(duckyluuk), 306(Yuchen20)
def p(g):
 d=[1,0,-1,0,1]
 for k in range(16):
  for i in range(len(g)):
   for j in range(len(g)):
    y,x=i,j
    if g[y][x]==3:
     a=3-k//4
     c=0
     o=0
     t=[s*1 for s in g]
     while 1:
      u,v=y+d[a],x+d[a+1]
      if len(g)>u>-1<v<len(g):
       if t[u][v]==8:
        a=(a+(k>>c&1)*2-1)%4
        c+=1
        if c>2:
         break
        continue
       if t[u][v]==2:
        if o:
         return t
        break
       if t[u][v]==3:
        o=1
      else:
       break
      t[u][v]=3
      y,x=u,v

# def p(g):
#  n=len(g)
#  for t in range(16):
#   r=t
#   a=str(g).find("3, 3")
#   if a>0:
#    i=a//(3*n+2)
#    j=a%(3*n+2)//3
#    u=[[*s]for s in g]
#    for c in [8,8,2]:
#     if c not in u[i][j:]:
#      break
#     k=u[i].index(c,j)
#     if 8 in u[i][j:k]:
#      break
#     u[i][j:k]=[3]*(k-j)
#     j=k-1
#     for _ in range(3-t//4%2*2):
#      r+=1
#      u=[[*s]for s in zip(*u[::-1])]
#      i,j=j,n-1-i
#     t//=2
#    else:
#     for _ in range(-r%4):
#      u=[[*s]for s in zip(*u[::-1])]
#     return u
#   g=[[*s]for s in zip(*g[::-1])]
#  return g
 

# def p(g):
#  n=len(g)
#  R=range(n*n)
#  for v in[e:=1,1,1,0]*2:
#   a,b,*_=[I for I in R if g[I//n][I%n]==3]
#   y=[I for I in R if g[I//n][I%n]==2][0]
#   l=r=[*g[b//n],8].index(8,b%n)
#   u=[*[s[r-1] for s in g],8].index(8,b//n)
#   w=y%n
#   if l>w:l,w=w+2,l
#   if(abs(a-b)==e)*(u==y//n+1)*~-(8*(r<n)in g[y//n][l:w]):
# #   if(abs(a-b)==e)*(u==y//n+1)*~-(8 in g[y//n][l:w])*(r<n):
#    g[b//n][b%n+1:r]=[3]*(r-b%n-1)
#    for s in g[b//n:u]:s[r-1]=e=3
# #    for i in R(b//n,u):g[i][r-1]=3
#    g[y//n][l:w]=[3]*(w-l)
#   if v:g=g[::-1]
#   # *g,=map(list,zip(*g))
#   g[:]=map(list,zip(*g))
#  return g


# def p(g):
#  n=len(g)
#  e=1
#  for _ in range(8):
#   x=[I for I in range(n*n) if g[I//n][I%n]==3]
#   y=[I for I in range(n*n) if g[I//n][I%n]==2][0]
#   r=(g[x[1]//n]+[8]).index(8,x[1]%n)
#   u=([g[i][r-1] for i in range(n)]+[8]).index(8,x[1]//n)
#   w=r
#   l=y%n+2
#   if l>w:l,w=r,l-2
#   if abs(x[0]-x[1])==e and u==y//n+1 and 8 not in g[y//n][l:w] and r<n:
#    g[x[1]//n][x[1]%n+1:r] = [3]*(r-x[1]%n-1)
#    for i in range(x[1]//n,u):g[i][r-1]=3
#    g[y//n][l:w] = [3]*(w-l)
#    e=0
#   *g,=map(list,zip(*g[::-1]))
#   if _%4==3:
#    g=g[::-1]
#  return g
