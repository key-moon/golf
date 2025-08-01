def p(g):
    R,C = len(g), len(g[0])
    # collect all nonzero cells
    S = {(r,c) for r in range(R) for c in range(C) if g[r][c]}
    if not S: return g
    # find endpoints = cells in S with exactly one S‐neighbor
    neigh = [(1,0),(-1,0),(0,1),(0,-1)]
    ends = [p for p in S if sum(((p[0]+dr,p[1]+dc) in S) for dr,dc in neigh)==1]
    start, end = ends
    # BFS to get the unique path from start to end
    from collections import deque
    q=deque([start]); parent={start:None}
    while q:
        u=q.popleft()
        if u==end: break
        for dr,dc in neigh:
            v = (u[0]+dr, u[1]+dc)
            if v in S and v not in parent:
                parent[v]=u; q.append(v)
    # reconstruct the path in order
    path=[]
    u=end
    while u:
        path.append(u)
        u=parent[u]
    path = path[::-1]
    # build the step‐vector list
    steps = [(path[i+1][0]-path[i][0], path[i+1][1]-path[i][1])
             for i in range(len(path)-1)]
    # now march out from the 'end' along repeating steps
    color = g[end[0]][end[1]]
    cur   = end
    i     = 0
    while True:
        dr,dc = steps[i % len(steps)]
        nxt = (cur[0]+dr, cur[1]+dc)
        if not (0<=nxt[0]<R and 0<=nxt[1]<C): break
        if g[nxt[0]][nxt[1]]!=0:       break
        g[nxt[0]][nxt[1]] = color
        cur = nxt
        i  += 1
    return g
