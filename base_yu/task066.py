# best: 268(4atj sisyphus luke Seek mukundan) / others: 289(xsot ovs att joking mewheni), 290(jailctf merger), 299(natte), 303(duckyluuk), 305(Yuchen20)
def p(g):
 n=len(g)
 R=range(n*n)
 for v in[e:=1,1,1,0]*2:
  a,b,*_=[I for I in R if g[I//n][I%n]==3]
  y=[I for I in R if g[I//n][I%n]==2][0]
  l=r=[*g[b//n],8].index(8,b%n)
  u=[*[s[r-1] for s in g],8].index(8,b//n)
  w=y%n
  if l>w:l,w=w+2,l
  if(abs(a-b)==e)*(u==y//n+1)*~-(8*(r<n)in g[y//n][l:w]):
#   if(abs(a-b)==e)*(u==y//n+1)*~-(8 in g[y//n][l:w])*(r<n):
   g[b//n][b%n+1:r]=[3]*(r-b%n-1)
   for s in g[b//n:u]:s[r-1]=e=3
#    for i in R(b//n,u):g[i][r-1]=3
   g[y//n][l:w]=[3]*(w-l)
  if v:g=g[::-1]
  *g,=map(list,zip(*g))
 return g


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
