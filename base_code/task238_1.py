def p(g):
    val_r,val_c=len(g),len(g[0])
    val_d={}
    for val_y in range(val_r):
        for val_x in range(val_c):
            val_v=g[val_y][val_x]
            if val_v: val_d.setdefault(val_v,[]).append((val_x,val_y))
    val_H=[];val_V=[]
    for val_v,val_pts in val_d.items():
        val_xs,val_ys=zip(*val_pts)
        val_ax,val_ax2,min_y,val_ay=min(val_xs),max(val_xs),min(val_ys),max(val_ys)
        val_w,val_h=val_ax2-val_ax,val_ay-min_y
        if val_w and val_h:
            val_P,val_x0,val_y0,val_s=val_v,val_ax,min_y,val_w+1
        elif val_h==0:
            val_H.append((min_y,val_v))
        else:
            val_V.append((val_ax,val_v))
    val_H.sort();val_V.sort()
    val_T=val_H[0][1];val_B=val_H[-1][1]
    val_L=val_V[0][1];val_R=val_V[-1][1]
    val_N=val_s+2
    val_o=[[0]*val_N for _ in range(val_N)]
    for val_i in range(1,val_N-1):
        val_o[0][val_i]=val_T; val_o[-1][val_i]=val_B
        val_o[val_i][0]=val_L; val_o[val_i][-1]=val_R
    for val_x,val_y in val_d[val_P]:
        val_o[val_y-val_y0+1][val_x-val_x0+1]=val_P
    return val_o
