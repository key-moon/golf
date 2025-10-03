A=range
def p(g):
 u=v=w=0
 for i in A(21):
  for j in A(21):
   if(t:=sum((g[c][d]==g[y][x]>0)-.9for x in A(10)for y in A(10)if-1<(c:=i-y-1)<10if-1<(d:=j-x-1)<10if max(abs(c-y),abs(d-x))<3))>w:u,v,w=i-j,i+j,t
 for k in A(400):
  if g[y:=k%10][x:=k//10%10]>0:g[u//2+x][v//2-1-y]=g[y][x]
 return g