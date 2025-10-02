C=enumerate
A=range
def p(g):
 h,w=len(g),len(g[0]);B=sum(g,[]);_,k,c=min((B.count(v),i,v)for(i,v)in C(B));_,l=max((abs(i-k)+abs(i%w-k%w)*2,i)for(i,v)in C(B)if v<1)
 for i in A(h):
  for j in A(w):
   for t in A(9*(g[i][j]<1)):
    if-1<(y:=i-~t*(k//w-l//w))<h and-1<(x:=j-~t*(k%w-l%w))<w:g[y][x]=c
 return g