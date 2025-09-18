def p(g):
    # collect the two colored points
    val_s=[(y,x,v)
           for y,row in enumerate(g)
           for x,v in enumerate(row)
           if v]
    y1,x1,v1=val_s[0]; y2,x2,v2=val_s[1]
    # if they share a row, build a horizontal stem + vertical arms
    if y1==y2:
        y=y1
        dx=1 if x2>x1 else -1
        m=(x2-x1)*dx//2
        c=(x1+x2)//2
        # two arms along the row
        for i in range(m+1):
            g[y][x1+dx*i]=v1
            g[y][x2-dx*i]=v2
        # two arms up/down from the midpoint
        for i in range(1,m+1):
            g[y-i][c]=v1
            g[y+i][c]=v2
    # else they share a column, build a vertical stem + horizontal arms
    else:
        x=x1
        dy=1 if y2>y1 else -1
        m=(y2-y1)*dy//2
        r=(y1+y2)//2
        # two arms along the column
        for i in range(m+1):
            g[y1+dy*i][x]=v1
            g[y2-dy*i][x]=v2
        # two arms left/right from the midpoint
        for i in range(1,m+1):
            g[r][x-i]=v1
            g[r][x+i]=v2
    return g
