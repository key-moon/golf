def p(g):
    val_h,val_w=len(g),len(g[0]);val_d={}
    for val_i in range(val_h):
        val_c=g[val_i][0]
        if val_c and g[val_i].count(val_c)==val_w:
            val_d.setdefault(val_c,[]).append((1,val_i))
    for val_j in range(val_w):
        val_c=g[0][val_j]
        if val_c and all(g[val_i][val_j]==val_c for val_i in range(val_h)):
            val_d.setdefault(val_c,[]).append((0,val_j))
    for val_x,val_row in enumerate(g):
        for val_y,val_v in enumerate(val_row):
            for val_t,val_k in val_d.get(val_v,()):
                if val_t and val_x!=val_k:
                    g[val_k+(1 if val_x>val_k else -1)][val_y]=val_v
                if not val_t and val_y!=val_k:
                    g[val_x][val_k+(1 if val_y>val_k else -1)]=val_v
    return g
