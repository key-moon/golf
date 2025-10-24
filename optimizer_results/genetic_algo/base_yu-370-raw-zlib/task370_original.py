D=enumerate
C=sum
B=range
A=len
def p(g):
 _,k,c=min((C(g,[]).count(v),i,v)for(i,v)in D(C(g,[])));_,l=max((abs(i-k)+abs(i%A(g[0])-k%A(g[0]))*2,i)for(i,v)in D(C(g,[]))if v<1)
 for i in B(A(g)):
  for j in B(A(g[0])):
   for t in B(9):
    if g[i][j]<1and i-~t*(k//A(g[0])-l//A(g[0]))in B(A(g))and j-~t*(k%A(g[0])-l%A(g[0]))in B(A(g[0])):g[i-~t*(k//A(g[0])-l//A(g[0]))][j-~t*(k%A(g[0])-l%A(g[0]))]=c
 return g