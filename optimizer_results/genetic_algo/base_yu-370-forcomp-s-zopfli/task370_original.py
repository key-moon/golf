def p(g):
 h,w=len(g),len(g[0]);A=sum(g,[]);_,k,c=min((A.count(v),i,v)for(i,v)in enumerate(A));_,l=max((abs(i-k)+abs(i%w-k%w)*2,i)for(i,v)in enumerate(A)if v<1)
 for i in range(h):
  for j in range(w):
   for t in range(9*(g[i][j]<1)):
    if-1<(y:=i-~t*(k//w-l//w))<h and-1<(x:=j-~t*(k%w-l%w))<w:g[y][x]=c
 return g