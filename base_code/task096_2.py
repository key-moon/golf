def p(g):
    h,w=len(g),len(g[0])
    # find background = most frequent color
    cnt={}
    for R in g:
        for x in R:
            cnt[x]=cnt.get(x,0)+1
    bg=max(cnt,key=cnt.get)
    # collect all non-bg points
    P=[(i,j) for i in range(h) for j in range(w) if g[i][j]!=bg]
    ys=sorted({i for i,_ in P})
    xs=sorted({j for _,j in P})
    # find runs of consecutive ys -> block height list
    def runs(a):
        R=[];s=[a[0]]
        for u,v in zip(a,a[1:]):
            if v==u+1: s.append(v)
            else:
                R.append(s);s=[v]
        R.append(s)
        return R
    ry=runs(ys);rx=runs(xs)
    bh=len(ry[0]);bw=len(rx[0])
    nbY=len(ry);nbX=len(rx)
    # new size = nb*block + (nb-1) gaps of size 1
    H=nbY*bh+(nbY-1);W=nbX*bw+(nbX-1)
    R=[[bg]*W for _ in range(H)]
    # for each block in input, extract its little rectangle and paste
    for by,yrun in enumerate(ry):
        for bx,xrun in enumerate(rx):
            # take bounding box of this block
            h0,h1=yrun[0],yrun[-1]
            w0,w1=xrun[0],xrun[-1]
            ph, pw = h1-h0+1, w1-w0+1
            # copy it
            blk=[g[i][w0:w1+1] for i in range(h0,h1+1)]
            # where to paste
            i0=by*(bh+1)
            j0=bx*(bw+1)
            for di in range(ph):
                for dj in range(pw):
                    R[i0+di][j0+dj]=blk[di][dj]
    return R
