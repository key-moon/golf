def p(g):
    val_h,val_w=len(g),len(g[0])
    val_m=[val_h]*5; val_M=[-1]*5
    for y,row in enumerate(g):
        for x,v in enumerate(row):
            if v:
                if y<val_m[v]: val_m[v]=y
                if y>val_M[v]: val_M[v]=y
    val_o=[[0]*val_w for _ in g]
    for y,row in enumerate(g):
        for x,v in enumerate(row):
            if v:
                # shift up by its own height=(max_row-min_row+1)
                val_o[y-(val_M[v]-val_m[v]+1)][x]=v
    return val_o
