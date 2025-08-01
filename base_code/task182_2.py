def p(g):
    val_h,val_w=len(g),len(g[0])
    # 1) find the 5-frame bounding box
    val_y0,val_x0,val_y1,val_x1=val_w,val_h,0,0
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j]==5:
                if val_i<val_y0: val_y0=val_i
                if val_j<val_x0: val_x0=val_j
                if val_i>val_y1: val_y1=val_i
                if val_j>val_x1: val_x1=val_j
    # 2) extract the interior mask P and its color c1
    val_P={(val_i-val_y0-1,val_j-val_x0-1)
           for val_i in range(val_y0+1,val_y1)
           for val_j in range(val_x0+1,val_x1)
           if g[val_i][val_j] not in (0,5)}
    val_d=next(iter(val_P))
    val_c1=g[val_y0+1+val_d[0]][val_x0+1+val_d[1]]
    # 3) flood-fill all other nonzero≠5 components, match mask and recolor
    val_v=[[0]*val_w for _ in g]
    for val_i in range(val_h):
        for val_j in range(val_w):
            val_c=g[val_i][val_j]
            if val_c and val_c!=5 and not val_v[val_i][val_j]:
                val_F=[(val_i,val_j)];val_v[val_i][val_j]=1
                for val_k in range(len(val_F)):
                    val_y,val_x=val_F[val_k]
                    for val_da,val_db in((1,0),(-1,0),(0,1),(0,-1)):
                        val_ni,val_nj=val_y+val_da,val_x+val_db
                        if 0<=val_ni<val_h and 0<=val_nj<val_w \
                           and not val_v[val_ni][val_nj] \
                           and g[val_ni][val_nj]==val_c:
                            val_v[val_ni][val_nj]=1
                            val_F.append((val_ni,val_nj))
                val_fy,val_fx=val_F[0]
                # skip the one inside the 5-frame
                if not(val_y0<val_fy<val_y1 and val_x0<val_fx<val_x1):
                    val_my,val_mx=val_h,val_w
                    for val_q,val_r in val_F:
                        if val_q<val_my: val_my=val_q
                        if val_r<val_mx: val_mx=val_r
                    if {(val_q-val_my,val_r-val_mx) for val_q,val_r in val_F}==val_P:
                        for val_q,val_r in val_F:
                            g[val_q][val_r]=val_c1
    return g
