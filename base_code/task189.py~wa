def p(g):
    h,len0=len(g),len(g[0])
    for r in range(h):
        x=g[r][0]
        if x and g[r].count(x)==len0:
            m=x
            break
    for c in range(len0):
        if all(g[i][c]==m for i in range(h)):
            break
    for dr in (0,r+1):
        nr=r if dr<r else h-r-1
        for dc in (0,c+1):
            nc=c if dc<c else len0-c-1
            if nr==2==nc:
                B=[g[dr][dc:dc+2],g[dr+1][dc:dc+2]]
    O=[[0]*6 for _ in[0]*6]
    for i in (0,1):
        for j in (0,1):
            v=B[i][j]
            for k in (1,3,4,5,7):
                O[3*i+k//3][3*j+k%3]=v
    return O
