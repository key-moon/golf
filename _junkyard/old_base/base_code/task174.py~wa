def p(g):
    d = {}
    for i, r in enumerate(g):
        for j, c in enumerate(r):
            if c:
                m = d.get(c)
                if m:
                    m[:4] = [min(m[0], i), min(m[1], j), max(m[2], i), max(m[3], j)]
                    m[4] += 1
                else:
                    d[c] = [i, j, i, j, 1]
    for k, v in d.items():
        if v[4] == k:
            x, y, u, w, _ = v
            break
    return [[k if g[i][j] == k else 0 for j in range(y, w + 1)]
            for i in range(x, u + 1)]
