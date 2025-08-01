def p(g):
    val_a=[(val_i,val_j)for val_i,val_row in enumerate(g)for val_j,val_v in enumerate(val_row)if val_v==4];val_r0=min(val_i for val_i,_ in val_a);val_r1=max(val_i for val_i,_ in val_a);val_c0=min(val_j for _,val_j in val_a);val_c1=max(val_j for _,val_j in val_a);return [val_row[val_c0:val_c1+1]for val_row in g[val_r0:val_r1+1]]
