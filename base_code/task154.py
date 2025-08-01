def p(g):
    val_h,val_w=len(g),len(g[0])
    val_C=[(y,x)for y in range(val_h)for x in range(val_w)if g[y][x]==2]
    y0=min(y for y,x in val_C);y1=max(y for y,x in val_C)
    x0=min(x for y,x in val_C);x1=max(x for y,x in val_C)
    val_D=[(y,x)for y in range(val_h)for x in range(val_w)if g[y][x]==5]
    val_E=set(val_D);val_F=[]
    while val_E:
        y,x=val_E.pop();val_Q=[(y,x)];val_c=[(y,x)]
        while val_Q:
            Y,X=val_Q.pop()
            for dY,dX in((1,0),(-1,0),(0,1),(0,-1)):
                v=(Y+dY,X+dX)
                if v in val_E:
                    val_E.remove(v);val_Q.append(v);val_c.append(v)
        val_F.append(val_c)
    for y,x in val_D: g[y][x]=0
    for val_c in val_F:
        ys=[y for y,x in val_c]; xs=[x for y,x in val_c]
        r0,r1=y0+1-min(ys),y1-1-max(ys)
        c0,c1=x0+1-min(xs),x1-1-max(xs)
        bd=10**9
        for dY in range(r0,r1+1):
            for dX in range(c0,c1+1):
                ok=1
                for y,x in val_c:
                    if g[y+dY][x+dX]!=0: ok=0; break
                if ok:
                    d=abs(dY)+abs(dX)
                    if d<bd: bd=d; ty,tx=dY,dX
        for y,x in val_c: g[y+ty][x+tx]=5
    return g
