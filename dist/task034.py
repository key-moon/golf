C=enumerate
def p(g):u=sum(g,[]);A,B=divmod(u.index(max(u,key=bool)),9);return[[sum({*u}-{2})*(v>0 or g[A+(r>A)][B+(c>B)]==2>min(abs(r-c-A+B),abs(r+c-A-B-1)))for(c,v)in C(D)]for(r,D)in C(g)]