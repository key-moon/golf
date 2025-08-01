def p(g):
    val_T=[(i,j,v)for i,row in enumerate(g)for j,v in enumerate(row)if v and v!=8]
    if not val_T: return g
    val_a=min(i for i,j,v in val_T); val_b=min(j for i,j,v in val_T)
    val_X=[(i-val_a,j-val_b,v)for i,j,v in val_T]
    val_M=[(i,j)for i,row in enumerate(g)for j,v in enumerate(row)
           if v==8 and (i==0 or g[i-1][j]!=8) and (j==0 or row[j-1]!=8)]
    for i,row in enumerate(g): g[i]=[0]*len(row)
    for a,b in val_M:
        for di,dj,v in val_X: g[a+di][b+dj]=v
    return g
