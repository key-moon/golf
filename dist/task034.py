D=enumerate
C=sum
def p(g):u=C(g,[]);A,B=divmod(u.index(max(u,key=bool)),9);return[[[0,C({*C(g,[])})-2][0<=r-A<2and 0<=c-B<2or g[A+(r>A)][B+(c>B)]==2and[(r-c-A+B)**2<2,0<=r+c-A-B<3][(r>A)^(c>B)]]for(c,_)in D(E)]for(r,E)in D(g)]