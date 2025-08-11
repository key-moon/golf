def p(g):
    n=len(g)
    # find the two bar‐rows (all 5s) and two bar‐cols
    rs=[i for i,row in enumerate(g) if all(x==5 for x in row)]
    cs=[j for j in range(n) if all(g[i][j]==5 for i in range(n))]
    # split into 3×3 blocks of size b
    rs=[-1]+rs+[n]; cs=[-1]+cs+[n]
    b1=rs[1]-rs[0]-1
    out=[row[:] for row in g]
    for bi in range(3):
        for bj in range(3):
            r0=rs[bi]+1; c0=cs[bj]+1
            blk=[g[r][c] for r in range(r0,r0+b1)
                         for c in range(c0,c0+b1)]
            # pick most common non-zero; if tie or none, pick median of non-zeros; else 0
            cnt={}
            for x in blk:
                if x and x!=5: cnt[x]=cnt.get(x,0)+1
            if cnt:
                m=max(cnt.values())
                cands=[x for x,v in cnt.items() if v==m]
                if len(cands)>1: c=min(cnt) if m>1 else sorted(cnt)[len(cnt)//2]
            else:
                c=0
            for i in range(r0,r0+b1):
                for j in range(c0,c0+b1):
                    out[i][j]=c
    return out
