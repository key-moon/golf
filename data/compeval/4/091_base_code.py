def p(g):
    val_rc=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==5]
    val_rs,val_cs=zip(*val_rc)
    val_r0,val_r1=min(val_rs)-1,max(val_rs)+1
    val_r0,max_r0=max(val_r0,0),None
    val_r1,min_r1=min(val_r1,len(g)-1),None
    val_c0,val_c1=min(val_cs),max(val_cs)
    return [row[val_c0:val_c1+1] for row in g[val_r0:val_r1+1]]
