def p(g):
    s = max(map(max, g))
    b, o = (4, 3) if s == 9 else (3, 4)
    m, n = len(g), len(g[0])
    vis = [[0]*n for _ in g]
    st = []
    # seed from borders
    for i in range(m):
        for j in (0, n-1):
            if g[i][j] != s and not vis[i][j]:
                vis[i][j] = 1
                st.append((i, j))
    for j in range(n):
        for i in (0, m-1):
            if g[i][j] != s and not vis[i][j]:
                vis[i][j] = 1
                st.append((i, j))
    # flood‐fill background
    while st:
        i, j = st.pop()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            x, y = i+di, j+dj
            if 0 <= x < m and 0 <= y < n and g[x][y] != s and not vis[x][y]:
                vis[x][y] = 1
                st.append((x, y))
    # recolor
    for i in range(m):
        for j in range(n):
            if g[i][j] != s:
                g[i][j] = b if vis[i][j] else o
    return g
