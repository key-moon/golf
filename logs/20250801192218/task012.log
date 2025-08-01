def p(g):
    H,W=len(g),len(g[0])
    o=[[0]*W for _ in g]
    for y in range(2,H-2):
        for x in range(2,W-2):
            C=g[y][x]; D=g[y-1][x]
            if C and D and g[y+1][x]==D==g[y][x-1]==g[y][x+1]:
                for dy,dx in ((2,0),(1,0),(0,1),(0,2),(-1,0),(0,-1),(0,-2),(-2,0),
                               (1,1),(1,-1),(-1,1),(-1,-1),(0,0)):
                    o[y+dy][x+dx] = D if (dy*dx==0 and (dy or dx)) else C
    return o