def p(g):
    val_d={}
    for val_i,val_r in enumerate(g):
        for val_j,val_x in enumerate(val_r):
            if val_x: val_d.setdefault(val_x,[]).append((val_i,val_j))
    val_t=sorted(val_d,key=lambda val_k:len(val_d[val_k]))
    val_b,val_a=val_t[0],val_t[-1]
    val_pa,val_pb=val_d[val_a],val_d[val_b]
    val_r0,val_r1=min(v[0]for v in val_pa),max(v[0]for v in val_pa)
    val_c0,val_c1=min(v[1]for v in val_pa),max(v[1]for v in val_pa)
    val_h=(val_r1-val_r0+1)//3; val_w=(val_c1-val_c0+1)//3
    val_R=[[0]*3 for _ in[None]*3]
    for val_i,val_j in val_pb:
        val_R[(val_i-val_r0)//val_h][(val_j-val_c0)//val_w]=val_b
    return val_R
