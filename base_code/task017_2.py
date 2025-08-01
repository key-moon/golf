def p(g):
    val_r=[i for i,r in enumerate(g)if 0 not in r]
    val_c=[j for j in range(len(g[0]))if all(g[i][j]for i in range(len(g)))]
    val_t=[[g[i][j]for j in val_c]for i in val_r]
    return [[val_t[i%len(val_r)][j%len(val_c)]for j in range(len(g[0]))]for i in range(len(g))]
