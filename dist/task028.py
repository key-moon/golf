B=range
A=enumerate
def p(g):
 n=len(g);C=sorted((i,j,v)for(i,r)in A(g)for(j,v)in A(r)if v);a,_,u=C[0];b,_,w=C[-1]
 for i in B(1,n-1):g[i][0]=g[i][-1]=u if i*2<=a+b else w
 for j in B(n):g[0][j]=g[a][j]=u;g[b][j]=g[-1][j]=w
 return g