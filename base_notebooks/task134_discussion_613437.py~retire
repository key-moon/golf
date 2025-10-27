E=enumerate
def p(m,*Q):
    for c in(f:={*sum(m,[])}-{0}):Y,X=zip(*[(y,x)for y,r in E(m)for x,v in E(r)if v==c]);Q+=(max(Y)-min(Y)+1,c,min(Y),min(X)),
    n,c,y,x=min(Q);return[[(v==c)*sum(f,-c)for v in r[x:x+n:n//3]]for r in m[y:y+n:n//3]]