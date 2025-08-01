def p(g):
    val_h,val_w=len(g),len(g[0])
    val_mp={}
    for i in range(val_h):
        for j in range(val_w):
            v=g[i][j]
            if v:
                val_mp.setdefault(v,[]).append((i,j))
    val_big=max(val_mp,key=lambda k:len(val_mp[k]))
    val_sml=min(val_mp,key=lambda k:len(val_mp[k]))
    cx,cy=val_mp[val_sml][0]
    for dx,dy in((1,1),(1,-1),(-1,1),(-1,-1)):
        k=1
        while True:
            x,y=cx+dx*k,cy+dy*k
            if x<0 or y<0 or x>=val_h or y>=val_w:break
            if g[x][y]==val_big:
                k+=1
                while True:
                    x,y=cx+dx*k,cy+dy*k
                    if x<0 or y<0 or x>=val_h or y>=val_w:break
                    g[x][y]=val_sml
                    k+=1
                break
            k+=1
    return g
