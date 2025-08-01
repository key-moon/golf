def p(g):
    n,m=len(g),len(g[0])
    𝛕=lambda v:(v[1],-v[0])  # cw90
    # find all straight 4‐segments
    segs=[]
    seen=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if g[i][j]==4 and not seen[i][j]:
                # try horizontal
                if j+1<m and g[i][j+1]==4:
                    t=[]
                    k=j
                    while k<m and g[i][k]==4:
                        seen[i][k]=1
                        t.append((i,k))
                        k+=1
                    segs.append((t,(0,1)))
                # or vertical
                elif i+1<n and g[i+1][j]==4:
                    t=[]
                    k=i
                    while k<n and g[k][j]==4:
                        seen[k][j]=1
                        t.append((k,j))
                        k+=1
                    segs.append((t,(1,0)))
    # reference = first segment
    T,ot=segs[0]
    L=len(T)
    # its two perp dirs
    st1,st2=𝛕(ot),(-𝛕(ot)[0],-𝛕(ot)[1])
    # collect patterns at its sides
    p1=[g[x+st1[0]][y+st1[1]] if 0<=x+st1[0]<n and 0<=y+st1[1]<m else 0
        for x,y in T]
    p2=[g[x+st2[0]][y+st2[1]] if 0<=x+st2[0]<n and 0<=y+st2[1]<m else 0
        for x,y in T]
    # for each segment fill missing side
    for S,ot2 in segs:
        # find rotation r: how many cw90 to send ot2 to ot
        r=0
        v=ot2
        for _ in range(4):
            if v==ot: break
            v=𝛕(v); r+=1
        # for each cell
        for k,(x,y) in enumerate(S):
            for q,(pp,sd) in enumerate(((p1,𝛕(ot2)),(p2,(-𝛕(ot2)[0],-𝛕(ot2)[1])))):
                i2,j2=x+sd[0],y+sd[1]
                if 0<=i2<n and 0<=j2<m and g[i2][j2]==0:
                    # map index k→k′; only rot==2 reverses
                    kk=k if r!=2 else L-1-k
                    g[i2][j2]=pp[kk]
    return g
