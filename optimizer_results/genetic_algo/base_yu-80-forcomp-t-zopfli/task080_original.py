C=sum
B=len
A=range
def p(g):
 a,*_,b,c=sorted({*C(g,[])},key=lambda c:(C(g,[]).count(c),C(g,[])[::-1].index(c)+C(g,[]).index(c)));s=C(g,[]).index(b^c)+1
 for i in A(B(g)):
  for j in A(B(g)):
   for y in A(B(g)):
    for x in A(B(g)):
     for k in-s,0,s:
      for l in-s,0,s:
       if g[i][j]==g[y][x]==a and i+k in A(B(g))and x+l in A(B(g))and y+k in A(B(g))and j+l in A(B(g)):g[y+k][x+l]|=g[i+k][j+l]
 return g