def p(g):
    n,m=len(g),len(g[0])
    # A = the output grid, start as a copy of g
    A=[row[:] for row in g]
    # mask holds all nonzeros so we can remove one shape at a time
    mask=[row[:] for row in g]

    # for each color
    for c in set(x for row in g for x in row if x):
        # collect all points of that color
        pts=[(i,j) for i in range(n) for j in range(m) if g[i][j]==c]
        # bounding box
        r0,r1=min(i for i,_ in pts),max(i for i,_ in pts)
        c0,c1=min(j for _,j in pts),max(j for _,j in pts)
        # extract the little pattern
        sh=[[g[i][j] for j in range(c0,c1+1)] for i in range(r0,r1+1)]
        h,w=len(sh),len(sh[0])
        # remove it from mask
        for i,j in pts:
            mask[i][j]=0

        # compute gap to nearest obstacle or border in each direction
        # RIGHT
        gapR=m
        for i in range(r0,r1+1):
            for j in range(c1+1,m):
                if mask[i][j]:
                    gapR=min(gapR,j-c1-1)
                    break
            else:
                gapR=min(gapR,m-c1-1)
        # LEFT
        gapL=m
        for i in range(r0,r1+1):
            for j in range(c0-1,-1,-1):
                if mask[i][j]:
                    gapL=min(gapL,c0-j-1)
                    break
            else:
                gapL=min(gapL,c0)
        # DOWN
        gapD=n
        for j in range(c0,c1+1):
            for i in range(r1+1,n):
                if mask[i][j]:
                    gapD=min(gapD,i-r1-1)
                    break
            else:
                gapD=min(gapD,n-r1-1)
        # UP
        gapU=n
        for j in range(c0,c1+1):
            for i in range(r0-1,-1,-1):
                if mask[i][j]:
                    gapU=min(gapU,r0-i-1)
                    break
            else:
                gapU=min(gapU,r0)

        # pick the direction with the largest free gap
        dir = max((gapR,'R'),(gapL,'L'),(gapD,'D'),(gapU,'U'))[1]
        # if there's no room, skip
        if {'R':gapR,'L':gapL,'D':gapD,'U':gapU}[dir]==0:
            continue

        # set the step vector
        dr,dc = {'R':(0,w),'L':(0,-w),'D':(h,0),'U':(-h,0)}[dir]
        # tile repeatedly
        k=1
        while True:
            rr,cc = r0+dr*k, c0+dc*k
            if not (0<=rr and rr+h<=n and 0<=cc and cc+w<=m):
                break
            # check overlap
            ok=True
            for i in range(h):
                for j in range(w):
                    if sh[i][j] and A[rr+i][cc+j]:
                        ok=False
                        break
                if not ok:
                    break
            if not ok:
                break
            # paste
            for i in range(h):
                for j in range(w):
                    if sh[i][j]:
                        A[rr+i][cc+j]=c
            k+=1

    # write back into g
    for i in range(n):
        g[i][:]=A[i]
    return g
