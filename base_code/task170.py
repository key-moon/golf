def p(g):
    H,W=len(g),len(g[0]);c={}
    for r in g:
        for x in r:
            if x:c[x]=c.get(x,0)+1
    M=max(c,key=c.get)
    m=H*W;a=b=c=d=u=v=p=q=m;b=d=v=q=-1
    for i in range(H):
        for j in range(W):
            x=g[i][j]
            if x==M:
                a,b,c,d=min(a,i),max(b,i),min(c,j),max(d,j)
            elif x:
                u,v,p,q=min(u,i),max(v,i),min(p,j),max(q,j)
    h,vv=v-u+1,q-p+1
    dr=(b-a)//(h-1) if h>1 else 0
    dc=(d-c)//(vv-1) if vv>1 else 0
    R=[row[p:q+1] for row in g[u:v+1]]
    for i in range(h):
        for j in range(vv):
            if g[a+dr*i][c+dc*j]!=M:
                R[i][j]=0
    return R
