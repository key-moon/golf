import math
from collections import Counter

def p(g):
    # crop off first and last column
    g = [r[1:-1] for r in g]
    H, W = len(g), len(g[0])
    # collect the "corner" points marked by 5
    P = [(i, j) for i in range(H) for j in range(W) if g[i][j] == 5]
    # find a fill‐color among the nonzero/non‐5 cells:
    cnt = Counter(c for row in g for c in row if c not in (0, 5))
    fill = min(cnt, key=lambda k: (cnt[k], k))
    # build convex hull of the 5‐points
    cx = sum(i for i, j in P) / len(P)
    cy = sum(j for i, j in P) / len(P)
    P.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    def cr(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    HULL = []
    for p in P + P[::-1]:
        while len(HULL) > 1 and cr(HULL[-2], HULL[-1], p) <= 0:
            HULL.pop()
        HULL.append(p)
    HULL.pop()
    # point‐in‐polygon test
    def inside(i, j):
        x = j + 0.5; y = i + 0.5; total = 0
        for (a, b), (c, d) in zip(HULL, HULL[1:] + HULL[:1]):
            dx1, dy1 = a - y, b - x
            dx2, dy2 = c - y, d - x
            total += math.atan2(dx1*dy2 - dy1*dx2, dx1*dx2 + dy1*dy2)
        return abs(total) > 1
    # build output
    out = []
    for i in range(H):
        row = []
        for j in range(W):
            if g[i][j] == 5:
                row.append(0)
            elif inside(i, j):
                row.append(fill)
            else:
                row.append(g[i][j])
        out.append(row)
    return out