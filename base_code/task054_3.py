def p(val_g):
    val_s={c for r in val_g for c in r}
    h=len(val_g);w=len(val_g[0])
    for y in range(1,h-1):
        for x in range(1,w-1):
            b=val_g[y][x];a=val_g[y-1][x]
            if b!=a==val_g[y+1][x]==val_g[y][x-1]==val_g[y][x+1]:
                c=min(val_s-{a,b})
                for dy,dx in[(-1,-1),(-1,1),(1,-1),(1,1)]:
                    val_g[y+dy][x+dx]=c
    return val_g
