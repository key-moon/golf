A=enumerate
def p(g):u,v=zip(*((i,j)for(i,r)in A(g)for(j,w)in A(r)if w));a,b,c,d=min(u),max(u),min(v),max(v);return[g[i][c:d+1]*2for i in range(a,b+1)]