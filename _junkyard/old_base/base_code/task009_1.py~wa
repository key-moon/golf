def p(g):
    H,W=len(g),len(g[0])
    # find frame (separator) rows: those rows entirely one colour
    FR=[i for i,row in enumerate(g) if row.count(row[0])==W]
    # the separator colour
    f=g[FR[0]][0]
    # find the separator columns by looking at one frame‐row
    FC=[j for j in range(W) if g[FR[0]][j]==f]
    R,C=len(FR)-1,len(FC)-1
    # build small block‐grid B of size R×C, sampling top‐left of each 2×2 cell
    B=[[g[FR[i]+1][FC[j]+1] for j in range(C)] for i in range(R)]
    # for each real colour x≠0 fill in straight lines between any two x's
    for x in {c for row in B for c in row} - {0}:
        # horizontal fills
        for i in range(R):
            js=[j for j in range(C) if B[i][j]==x]
            if len(js)>1:
                a,b=min(js),max(js)
                for j in range(a+1,b):
                    B[i][j]=x
        # vertical fills
        for j in range(C):
            is_=[i for i in range(R) if B[i][j]==x]
            if len(is_)>1:
                a,b=min(is_),max(is_)
                for i in range(a+1,b):
                    B[i][j]=x
    # write B back into the original grid
    for i in range(R):
        for j in range(C):
            x=B[i][j]
            if x:
                for r in range(FR[i]+1,FR[i+1]):
                    for c in range(FC[j]+1,FC[j+1]):
                        g[r][c]=x
    return g
