def p(g):
    # collect positions by color
    val_d={}
    for val_r,val_row in enumerate(g):
        for val_c,val_v in enumerate(val_row):
            if val_v: val_d.setdefault(val_v,[]).append((val_r,val_c))
    # centroid of the big cluster of 5s
    val_o=val_d[5]
    val_n=len(val_o)
    val_o0=sum(r for r,_ in val_o)/val_n
    val_o1=sum(c for _,c in val_o)/val_n
    # prepare empty 9×9 filled with 5s
    val_a=[[5]*9 for _ in[0]*9]
    # for each small cluster ≠5
    for val_k,val_L in val_d.items():
        if val_k-5:
            # centroid of this cluster
            val_u0=sum(r for r,_ in val_L)/len(val_L)
            val_v0=sum(c for _,c in val_L)/len(val_L)
            # relative shift in 3×3–block units, rounded
            val_dr=int(round((val_u0-val_o0)/3))
            val_dc=int(round((val_v0-val_o1)/3))
            # map so that (0,0)->(0,0),(2,2)->(2,2) becomes
            #      new = 2 - old
            val_R,val_C=2-val_dr,2-val_dc
            # top‐left corner of this cluster’s 3×3 window
            val_mr=min(r for r,_ in val_L)
            val_mc=min(c for _,c in val_L)
            # copy‐over (0→5)
            for val_i in (0,1,2):
                for val_j in (0,1,2):
                    val_a[val_R*3+val_i][val_C*3+val_j]=g[val_mr+val_i][val_mc+val_j] or 5
    return val_a
