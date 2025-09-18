def p(g):
    R,C = len(g), len(g[0])
    # 1) collect all coords of 3
    coords = [(i,j) for i in range(R) for j in range(C) if g[i][j]==3]
    seen = set()
    comps = []
    # 2) extract 4‐connected components
    for (i,j) in coords:
        if (i,j) in seen: continue
        stk = [(i,j)]
        comp = []
        seen.add((i,j))
        while stk:
            x,y = stk.pop()
            comp.append((x,y))
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                u,v = x+dx, y+dy
                if 0<=u<R and 0<=v<C and (u,v) not in seen and g[u][v]==3:
                    seen.add((u,v))
                    stk.append((u,v))
        comps.append(comp)
    # 3) for each comp build its shape‐offsets and anchor (minr,minc)
    anchors = []
    shapes = []
    for comp in comps:
        rs = [x for x,y in comp]
        cs = [y for x,y in comp]
        r0,c0 = min(rs), min(cs)
        anchors.append((r0,c0))
        shapes.append([(x-r0,y-c0) for x,y in comp])
    # 4) collect unique anchor‐rows & anchor‐cols
    rows = sorted({r for r,_ in anchors})
    cols = sorted({c for _,c in anchors})
    # 5) for every missing (r,c) in the Cartesian product fill in the shape with 8’s
    for r in rows:
        for c in cols:
            if (r,c) in anchors: continue
            for shape in shapes:
                for dr,dc in shape:
                    x,y = r+dr, c+dc
                    if 0<=x<R and 0<=y<C and g[x][y]==0:
                        g[x][y] = 8
    return g
