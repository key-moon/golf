def p(g):
    from collections import Counter, deque
    H, W = len(g), len(g[0])
    # pick the color that appears most
    c = Counter(v for row in g for v in row if v).most_common(1)[0][0]
    # build mask of c‐pixels
    m = [[g[y][x]==c for x in range(W)] for y in range(H)]
    # mark all 0–regions reachable from the border
    vis = [[0]*W for _ in range(H)]
    q = deque()
    for i in range(H):
        for j in (0, W-1):
            if not m[i][j]:
                vis[i][j] = 1
                q.append((i,j))
    for j in range(W):
        for i in (0, H-1):
            if not m[i][j] and not vis[i][j]:
                vis[i][j] = 1
                q.append((i,j))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            yy, xx = y+dy, x+dx
            if 0 <= yy < H and 0 <= xx < W and not m[yy][xx] and not vis[yy][xx]:
                vis[yy][xx] = 1
                q.append((yy,xx))
    # fill any non‐c cell not reached (i.e. interior) with c; zero out everything else
    for y in range(H):
        for x in range(W):
            g[y][x] = c if (m[y][x] or (g[y][x] and not vis[y][x])) else 0
    return g
