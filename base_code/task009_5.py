def p(g):
    h,w=len(g),len(g[0])
    # find frame‐color f by spotting a row with >w/2 of one color
    for R in g:
        for f in set(R):
            if R.count(f)>w/2: break
     else
        break
    # stripe‐rows and stripe‐cols
    sr=[i for i in range(h) if g[i].count(f)>w/2]
    sc=[j for j in range(w) if sum(g[i][j]==f for i in range(h))>h/2]
    br=[-1]+sr+[h]; bc=[-1]+sc+[w]
    from collections import defaultdict
    D=defaultdict(list)
    # collect block‐coordinates of each 2×2 sub‐block color
    for i,R in enumerate(g):
        if i in sr: continue
        r=sum(i>k for k in sr)
        for j,v in enumerate(R):
            if j in sc or v in (0,f): continue
            c=sum(j>k for k in sc)
            D[("h",v,r)].append(c)
            D[("v",v,c)].append(r)
    # connect same‐color blocks horizontally or vertically
    for (t,v,a),ls in D.items():
        b,e=min(ls),max(ls)
        if t=="h":
            for c in range(b,e+1):
                for ii in range(br[a]+1,br[a+1]):
                    for jj in range(bc[c]+1,bc[c+1]):
                        g[ii][jj]=v
        else:
            for r in range(b,e+1):
                for ii in range(br[r]+1,br[r+1]):
                    for jj in range(bc[a]+1,bc[a+1]):
                        g[ii][jj]=v
    return g
