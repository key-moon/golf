def p(g):
    m,n=len(g),len(g[0])
    # 1) extract the 2 shapes (colors≠0,5), record their relative masks, clear them
    D={}
    cs={c for row in g for c in row if c not in (0,5)}
    for c in cs:
        L=[(i,j) for i,row in enumerate(g) for j,v in enumerate(row) if v==c]
        mi=min(i for i,_ in L); mj=min(j for _,j in L)
        mask=tuple(sorted((i-mi,j-mj) for i,j in L))
        D[mask]=c
        for i,j in L: g[i][j]=0
    # 2) find each 5‐rectangle, locate its hole, match & fill
    for i in range(m):
        for j in range(n):
            if g[i][j]==5 and (i==0 or g[i-1][j]!=5) and (j==0 or g[i][j-1]!=5):
                # measure width
                w=1
                while j+w<n and g[i][j+w]==5: w+=1
                # measure height
                h=1
                while i+h<m and all(g[i+h][j+dx]==5 for dx in range(w)): h+=1
                # collect relative coords of the hole
                hole=tuple(sorted((x-i,y-j)
                                  for x in range(i,i+h)
                                  for y in range(j,j+w)
                                  if g[x][y]!=5))
                if hole in D:
                    c=D[hole]
                    for x in range(i,i+h):
                        for y in range(j,j+w):
                            if g[x][y]!=5:
                                g[x][y]=c
    return g
