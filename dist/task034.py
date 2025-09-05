D=enumerate
C=sum
def p(g):u=C(g,[]);A,B=divmod(u.index(max(u,key=bool)),9);return[[C({*C(g,[])}-{2})*(v>0 or g[A+(r>A)][B+(c>B)]==2>min(abs(r-c-A+B),abs(r+c-A-B-1)))for(c,v)in D(E)]for(r,E)in D(g)]