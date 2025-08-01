def p(g):
    R,C=len(g),len(g[0])
    # find 5‐frame
    rs=[i for i in range(R) if 5 in g[i]]
    cs=[j for j in range(C) if any(g[i][j]==5 for i in range(R))]
    r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
    # interior
    M=[g[i][c0+1:c1] for i in range(r0+1,r1)]
    # find 8‐bbox
    P=[(i,j) for i,row in enumerate(M) for j,v in enumerate(row) if v==8]
    if not P: return [[0]*3 for _ in range(3)]
    i0,i1=min(i for i,j in P),max(i for i,j in P)
    j0,j1=min(j for i,j in P),max(j for i,j in P)
    S=[row[j0:j1+1] for row in M[i0:i1+1]]
    h,w=len(S),len(S[0])
    # resample to 3×3
    out=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if S[int(i*h/3)][int(j*w/3)]==8: out[i][j]=8
    return out