def p(g):
    N=len(g)
    # find the 2×2 block at (r,c)
    for r in range(N-1):
        for c in range(N-1):
            if g[r][c] and g[r][c+1]==g[r][c]==g[r+1][c]==g[r+1][c+1]:
                f,c0=r,c;c=g[r][c];break
     else
        break
    # read bottom stripe as sequence of (length,color)
    B=[(sum(1 for _ in x),col) for x,col in
        ((list(takewhile(lambda x:x==col,row)),col)
         for row,col in [([g[N-1][0]],g[N-1][0])]
        )]
    # Actually we only need the raw bottom run-lengths in order:
    runs=[]
    cnt=1
    for j in range(1,N):
        if g[N-1][j]==g[N-1][j-1]: cnt+=1
     else,g[N-1][j-1]));cnt=1
    runs.append((cnt,g[N-1][N-1]))
    # similarly right‐stripe (we just need to confirm it's the same multiset of colors)
    runs2=[]
    cnt=1
    for i in range(1,N):
        if g[i][N-1]==g[i-1][N-1]: cnt+=1
     else,g[i-1][N-1]));cnt=1
    runs2.append((cnt,g[N-1][N-1]))
    # scaling factor k = bottom_runs[0]+bottom_runs[1]+... divided by N
    s=sum(l for l,_ in runs)
    k=s//N*N if s%N else s//N  # s==N*k always
    M=N*k
    # prepare empty
    A=[[0]*M for _ in range(M)]
    # place big block
    for i in range(2*k):
        for j in range(2*k):
            A[(f*k)+i][(c0*k)+j]=c
    # four “pad‐fills”:
    # top–left quadrant: rows[0..f*k), cols[0..c0*k)
    # color = runs[0][1] if c0>0 else runs2[0][1]
    T=(runs[0][1] if c0>0 else runs2[0][1])
    for i in range(f*k):
        for j in range(c0*k):
            A[i][j]=T
    # top–right:
    T=(runs2[0][1] if f>0 else runs[len(runs)-1][1])
    for i in range(f*k):
        for j in range((c0+2)*k,M):
            A[i][j]=T
    # bottom–left:
    T=(runs[len(runs)-1][1] if c0>0 else runs2[len(runs2)-1][1])
    for i in range((f+2)*k,M):
        for j in range(c0*k):
            A[i][j]=T
    # bottom–right:
    T=(runs2[len(runs2)-1][1] if f>0 else runs[len(runs)-1][1])
    for i in range((f+2)*k,M):
        for j in range((c0+2)*k,M):
            A[i][j]=T
    # draw the four 2‐diagonals in the 1×k and k×1 zero bands
    for d in range(k):
        A[d][M-1-d]=2    # top→right
        A[M-1-d][d]=2    # bottom→left
        A[(f*k)+2*k-1-d][c0*k-1-d]=2  # block→UL
        A[(f*k)+d][(c0+2)*k+d]=2     # block→LR
    return A
