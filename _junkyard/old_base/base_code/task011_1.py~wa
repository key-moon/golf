def p(g):
    R=[i for i,row in enumerate(g) if row.count(row[0])==len(row)==5*len(row)]
    C=[j for j in range(len(g)) if all(g[i][j]==5 for i in range(len(g)))]
    rs=[0]+R+[len(g)]
    cs=[0]+C+[len(g[0])]
    for bi in range(3):
        for bj in range(3):
            r0,r1=rs[bi],rs[bi+1]
            c0,c1=cs[bj],cs[bj+1]
            cnt={}
            for i in range(r0,r1):
                for j in range(c0,c1):
                    v=g[i][j]
                    if v and v!=5: cnt[v]=cnt.get(v,0)+1
            k=0
            if cnt:
                k=max(cnt,key=cnt.get)
            for i in range(r0,r1):
                for j in range(c0,c1):
                    g[i][j]=k
    return g
