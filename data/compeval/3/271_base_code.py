def p(g):
    val_s=[[[g[val_i+val_a][val_j+val_b]for val_b in(0,1,2)]for val_a in(0,1,2)]for val_i in range(len(g)-2)for val_j in range(len(g[0])-2)if all(g[val_i+val_a][val_j+val_b]for val_a in(0,1,2)for val_b in(0,1,2))]
    return max(val_s,key=lambda val_t:sum(val_x==1 for val_r in val_t for val_x in val_r))
