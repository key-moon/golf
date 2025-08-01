def p(g):
    val_i=next(i for i in range(len(g)) if len(set(g[i]))==1)
    val_j=next(j for j in range(len(g[0])) if len({r[j] for r in g})==1)
    for val_a in (range(val_i), range(val_i+1, len(g))):
        for val_b in (range(val_j), range(val_j+1, len(g[0]))):
            val_s=[[g[x][y] for y in val_b] for x in val_a]
            if len(set(sum(val_s,[])))>1: return val_s
