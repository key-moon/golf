def p(val_g):
    from itertools import chain
    val_R,val_C=len(val_g),len(val_g[0])
    val_f=list(chain.from_iterable(val_g))
    val_s=max(set(val_f),key=val_f.count)
    val_P=[(i,j)for i in range(val_R)for j in range(val_C)if val_g[i][j]==val_s]
    val_mnr,minc=min(r for r,_ in val_P),min(c for _,c in val_P)
    val_D=[(r-val_mnr,c-minc)for r,c in val_P]
    val_cs=sorted({x for x in val_f if x and x!=val_s})
    val_m={v:i for i,v in enumerate(val_cs)}
    val_h,val_w=max(r for r,_ in val_D)+1,max(c for _,c in val_D)+1
    val_O=[[0]*(len(val_cs)*val_w)for _ in range(val_R*val_h)]
    for i in range(val_R):
        for j,v in enumerate(val_g[i]):
            if v in val_m:
                M=val_m[v];B=i*val_h;Cj=M*val_w
                for dr,dc in val_D: val_O[B+dr][Cj+dc]=v
    return val_O
