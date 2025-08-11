def p(g):
    val_s={c for r in g for c in r}
    h=len(g);w=len(g[0])
    for y in range(1,h-1):
        for x in range(1,w-1):
            b=g[y][x];a=g[y-1][x]
            if b!=a==g[y+1][x]==g[y][x-1]==g[y][x+1]:
                c=min(val_s-{a,b})
                for dy,dx in[(-1,-1),(-1,1),(1,-1),(1,1)]:
                    g[y+dy][x+dx]=c
    return g
