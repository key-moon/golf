def p(g):
    for val_v in {c for val_R in g for c in val_R if c}:
        val_l = [(i,j) for i,val_R in enumerate(g) for j,c in enumerate(val_R) if c==val_v]
        val_rs = [i for i,j in val_l]; val_cs = [j for i,j in val_l]
        val_mr = max(set(val_rs), key=val_rs.count); val_mc = max(set(val_cs), key=val_cs.count)
        if val_rs.count(val_mr) > val_cs.count(val_mc):
            for i,j in val_l:
                if i != val_mr:
                    g[val_mr + (1 if i>val_mr else -1)][j] = val_v; g[i][j] = 0
        else:
            for i,j in val_l:
                if j != val_mc:
                    g[i][val_mc + (1 if j>val_mc else -1)] = val_v; g[i][j] = 0
    return g
