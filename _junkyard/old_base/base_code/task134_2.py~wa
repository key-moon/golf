def p(g):
    val_s=sum(g,[])
    val_c=sorted({*val_s},key=lambda x:-val_s.count(x))
    val_m=next(x for x in val_c if x)
    val_d=next((x for x in val_c if x and x!=val_m),0)
    val_sr=min(i for i,r in enumerate(g) if val_m in r)
    val_er=max(i for i,r in enumerate(g) if val_m in r)
    val_sc=min(j for i,r in enumerate(g) for j,v in enumerate(r) if v==val_m)
    val_ec=max(j for i,r in enumerate(g) for j,v in enumerate(r) if v==val_m)
    val_h=(val_er-val_sr+1)//3;val_w=(val_ec-val_sc+1)//3
    val_o=[[0]*3 for _ in[0]*3]
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v==val_d and val_sr<=i<=val_er and val_sc<=j<=val_ec:
                val_o[(i-val_sr)//val_h][(j-val_sc)//val_w]=val_d
    return val_o
