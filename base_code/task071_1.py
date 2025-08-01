def p(g):
    val_h,val_w=len(g),len(g[0]);val_cs={}
    for y in range(val_h):
        for x in range(val_w):
            v=g[y][x];v and val_cs.setdefault(v,[]).append((y,x))
    val_L=sorted(val_cs,key=lambda k:-len(val_cs[k]));oc,op=val_L[0],val_L[1]
    ys=[y for y,x in val_cs[op]];xs=[x for y,x in val_cs[op]]
    y0,y1,x0,x1=min(ys),max(ys),min(xs),max(xs)
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            if g[y][x]==op:g[y][x]=0
            elif g[y][x]==0 and any(
                0<=y+dy<val_h and 0<=x+dx<val_w and g[y+dy][x+dx]==oc
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1))
            ):g[y][x]=oc
    return g
