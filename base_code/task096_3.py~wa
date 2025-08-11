def p(g):
    h,w=len(g),len(g[0])
    # find background = most frequent
    from collections import Counter,deque
    cnt=Counter(x for r in g for x in r)
    bg=cnt.most_common(1)[0][0]
    # flood‐fill to find all non‐bg components
    seen=[[0]*w for _ in g]
    comps=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]!=bg and not seen[i][j]:
                col=g[i][j]
                q=deque([(i,j)])
                seen[i][j]=1
                ys, xs = [],[]
                while q:
                    y,x=q.popleft()
                    ys.append(y); xs.append(x)
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and g[ny][nx]==col:
                            seen[ny][nx]=1
                            q.append((ny,nx))
                r0,r1=min(ys),max(ys)
                c0,c1=min(xs),max(xs)
                comps.append((col,r0,r1,c0,c1))
    # sort into TL,TR,BL,BR by component‐box center vs center of grid
    cy=h/2; cx=w/2
    comps.sort(key=lambda x: (x[1]+x[2]<2*cy,x[3]+x[4]<2*cx))
    # extract the "inner" (strip one‐pixel border) subgrid of each box
    strs=[]
    for (col,r0,r1,c0,c1) in comps:
        sub=[row[c0+1:c1] for row in g[r0+1:r1]]
        strs.append((col,sub))
    # all sub‐boxes must be same size k×k
    k=len(strs[0][1])
    R=[[bg]*(2*k+1) for _ in range(2*k+1)]
    # paste into the 4 quadrants
    for idx,(col,sub) in enumerate(strs):
        dy=(idx//2)*(k+1)
        dx=(idx%2)*(k+1)
        for i in range(k):
            for j in range(k):
                if sub[i][j]!=bg:
                    R[dy+1+i][dx+1+j]=col
    return R
