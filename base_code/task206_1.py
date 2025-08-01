def p(g):
    val_s=[]
    for y,row in enumerate(g):
        for x,v in enumerate(row):
            if v==5: val_m=(y,x)
            elif v:  val_s.append((y,x,v))
    y0,y1=min(y for y,_,_ in val_s),max(y for y,_,_ in val_s)
    x0,x1=min(x for _,x,_ in val_s),max(x for _,x,_ in val_s)
    cy,cx=(y0+y1)//2,(x0+x1)//2
    dy,dx=val_m[0]-cy,val_m[1]-cx
    g[val_m[0]][val_m[1]]=0
    for y,x,v in val_s: g[y+dy][x+dx]=v
    return g
