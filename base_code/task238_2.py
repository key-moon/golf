def p(g):
    val_d={}
    for val_i,val_row in enumerate(g):
        for val_j,val_v in enumerate(val_row):
            if val_v: val_d.setdefault(val_v,[]).append((val_i,val_j))
    val_C=max(val_d,key=lambda k:len(val_d[k]))
    val_L0=val_d[val_C]
    val_y0,val_y1=min(y for y,x in val_L0),max(y for y,x in val_L0)
    val_x0,val_x1=min(x for y,x in val_L0),max(x for y,x in val_L0)
    val_h,val_w=val_y1-val_y0+1,val_x1-val_x0+1
    val_A=[[0]*(val_w+2) for _ in range(val_h+2)]
    for y,x in val_L0:
        val_A[y-val_y0+1][x-val_x0+1]=val_C
    for val_v,val_L in val_d.items():
        if val_v==val_C: continue
        y,x=val_L[0]
        if len(val_L)>1 and y==val_L[1][0]:
            (val_T if y<val_y0 else val_B)=val_v
        else:
            (val_Lt if x<val_x0 else val_Rt)=val_v
    val_A[0]    =[0]+[val_T]*val_w+[0]
    val_A[-1]   =[0]+[val_B]*val_w+[0]
    for i in range(1,val_h+1):
        val_A[i][0]=val_Lt
        val_A[i][-1]=val_Rt
    return val_A
