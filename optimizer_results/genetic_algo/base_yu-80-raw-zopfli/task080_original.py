C=range
B=sum
A=len
def p(g):
 a,*_,b,c=sorted({*B(g,[])},key=lambda c:(B(g,[]).count(c),B(g,[])[::-1].index(c)+B(g,[]).index(c)));s=B(g,[]).index(b^c)+1
 for i in C(A(g)):
  for j in C(A(g)):
   for y in C(A(g)):
    for x in C(A(g)):
     for k in-s,0,s:
      for l in-s,0,s:
       if g[i][j]==g[y][x]==a and-1<i+k<A(g)>j+l>-1<y+k<A(g)>x+l>-1:g[y+k][x+l]|=g[i+k][j+l]
 return g