def p(g):
    # Collect non‐zero cells by color
    d = {}
    for i, row in enumerate(g):
        for j, v in enumerate(row):
            if v:
                d.setdefault(v, []).append((i, j))
    # Sort colors by leftmost occurrence (min column)
    L = sorted(d.items(), key=lambda t: min(c for _, c in t[1]))
    # Extract color, relative coords, height and width
    S = []
    for c, P in L:
        xs, ys = zip(*P)
        mr, mc = min(xs), min(ys)
        h, w = max(xs) - mr + 1, max(ys) - mc + 1
        S.append((c, [(x - mr, y - mc) for x, y in P], h, w))
    # Unpack shapes
    (c1, s1, _, _), (c2, s2, h2, w2) = S
    s1set = set(s1)
    # Decide placement for shape2: try horizontal then vertical
    for sr2, sc2 in ((0, 3 - w2), (3 - h2, 0)):
        if all((x + sr2, y + sc2) not in s1set for x, y in s2):
            break
    # Build the 3×3 result
    A = [[0]*3 for _ in range(3)]
    for x, y in s1:
        A[x][y] = c1
    for x, y in s2:
        A[x + sr2][y + sc2] = c2
    return A
