def p(g): 
    for val_c in set(sum(g,[])):
        val_L=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==val_c]
        val_m,val_n=min(val_L);val_M,val_N=max(val_L)
        if val_M-val_m>1<val_N-val_n and all((i in(val_m,val_M)or j in(val_n,val_N))for i,j in val_L):
            return [r[val_n+1:val_N]for r in g[val_m+1:val_M]]
