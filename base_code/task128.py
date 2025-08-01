def p(g):
    # find bounding boxes for each color
    b={}
    for i,row in enumerate(g):
        for j,v in enumerate(row):
            if v:
                x0,y0,x1,y1=b.get(v,(15,15,0,0))
                b[v]=(min(x0,i),min(y0,j),max(x1,i),max(y1,j))
    # sort blocks by left edge
    L=sorted(((v, *b[v]) for v in b), key=lambda x: x[2])
    # unpack left/mid/right
    vL,x0L,y0L,x1L,y1L = L[0]
    vM,x0M,y0M,x1M,y1M = L[1]
    vR,x0R,y0R,x1R,y1R = L[2]
    hL,hM,hR=x1L-x0L+1,x1M-x0M+1,x1R-x0R+1
    wL,wM,wR=y1L-y0L+1,y1M-y0M+1,y1R-y0R+1
    # target cols: left at 1, right at 15-wR-1
    cL=1; cR=15-wR-1
    # target row for top–shapes so they clear bottom
    rT=min(15-max(hL,hR)-1, 15-max(hL,hR)-hM)//2
    # now mid sits under the gap
    mid=(cL+wL-1 + cR)//2
    cM=mid - wM//2
    rM=rT+max(hL,hR)
    # make fresh grid
    R=[[0]*15 for _ in g]
    # blit
    for v,(r0,c0,h,w) in ((vL,(rT,cL,hL,wL)),(vR,(rT,cR,hR,wR)),(vM,(rM,cM,hM,wM))):
        for i in range(h):
            for j in range(w):
                R[r0+i][c0+j]=v
    return R
