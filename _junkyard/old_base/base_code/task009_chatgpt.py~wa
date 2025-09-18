def p(g):
    h, w = len(g), len(g[0])
    grid = max(set(x for r in g for x in r if x), key=lambda x: sum(r.count(x) for r in g))
    hr = [-1] + [i for i in range(h) if all(x == grid for x in g[i])] + [h]
    vc = [-1] + [j for j in range(w) if all(g[i][j] == grid for i in range(h))] + [w]
    cell = [[0]*(len(vc)-1) for _ in range(len(hr)-1)]

    for i in range(len(hr)-1):
        for j in range(len(vc)-1):
            for y in range(hr[i]+1, hr[i+1]):
                for x in range(vc[j]+1, vc[j+1]):
                    v = g[y][x]
                    if v and v != grid:
                        cell[i][j] = v

    for r in cell:
        for c in set(r):
            if c:
                i0 = min(i for i,v in enumerate(r) if v==c)
                i1 = max(i for i,v in enumerate(r) if v==c)
                for k in range(i0, i1+1):
                    if r[k]==0:
                        r[k]=c

    for j in range(len(vc)-1):
        col = [cell[i][j] for i in range(len(hr)-1)]
        for c in set(col):
            if c:
                i0 = min(i for i,v in enumerate(col) if v==c)
                i1 = max(i for i,v in enumerate(col) if v==c)
                for k in range(i0, i1+1):
                    if cell[k][j]==0:
                        cell[k][j]=c

    for i in range(len(hr)-1):
        for j in range(len(vc)-1):
            if cell[i][j]:
                for y in range(hr[i]+1, hr[i+1]):
                    for x in range(vc[j]+1, vc[j+1]):
                        g[y][x] = cell[i][j]
    return g
