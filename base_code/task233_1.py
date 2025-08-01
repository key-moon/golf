def p(g):
    val_a,val_b=zip(*[(i,j)for i,row in enumerate(g)for j,x in enumerate(row)if x==2])
    val_a0,val_a1=min(val_a),max(val_a)
    val_b0,val_b1=min(val_b),max(val_b)
    return [[g[i][j] or 2 for j in range(val_b0,val_b1+1)]
            for i in range(val_a0,val_a1+1)]
