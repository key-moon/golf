def p(val_g):
    val_h=len(val_g);val_w=len(val_g[0])
    val_seen=[[0]*val_w for _ in range(val_h)]
    for val_y in range(val_h):
        for val_x in range(val_w):
            if not val_seen[val_y][val_x]:
                val_c=val_g[val_y][val_x]
                val_seen[val_y][val_x]=1
                val_comp=[(val_x,val_y)]
                for val_i in range(len(val_comp)):
                    x0,y0=val_comp[val_i]
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        x1,y1=x0+dx,y0+dy
                        if 0<=x1<val_w and 0<=y1<val_h and not val_seen[y1][x1] and val_g[y1][x1]==val_c:
                            val_seen[y1][x1]=1; val_comp.append((x1,y1))
                xs=[x for x,y in val_comp]; ys=[y for x,y in val_comp]
                x0,x1,y0,y1=min(xs),max(xs),min(ys),max(ys)
                val_anoms=[(x,y) for y in range(y0,y1+1) for x in range(x0,x1+1) if val_g[y][x]!=val_c]
                if len(val_anoms)==1:
                    ax,ay=val_anoms[0]; m=val_g[ay][ax]
                    for fx in(0,1):
                        for fy in(0,1):
                            x2=(x0+x1-ax) if fx else ax
                            y2=(y0+y1-ay) if fy else ay
                            if val_g[y2][x2]==val_c: val_g[y2][x2]=m
                    val_g[ay][ax]=val_c
    return val_g
