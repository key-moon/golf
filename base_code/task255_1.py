def p(g):
    val_h=len(g);val_w=len(g[0])
    val_cnt={}
    for val_row in g:
        for val_c in val_row:
            val_cnt[val_c]=val_cnt.get(val_c,0)+1
    val_bg=max(val_cnt,key=val_cnt.get)
    val_s=[]
    for val_i in range(val_h):
        for val_j in(0,val_w-1):
            if g[val_i][val_j]==val_bg:val_s.append((val_i,val_j))
    for val_j in range(val_w):
        for val_i in(0,val_h-1):
            if g[val_i][val_j]==val_bg:val_s.append((val_i,val_j))
    while val_s:
        val_i,val_j=val_s.pop()
        if g[val_i][val_j]==val_bg:
            g[val_i][val_j]=-1
            for val_dr,val_dc in((1,0),(-1,0),(0,1),(0,-1)):
                val_ni,val_nj=val_i+val_dr,val_j+val_dc
                if 0<=val_ni<val_h and 0<=val_nj<val_w and g[val_ni][val_nj]==val_bg:
                    val_s.append((val_ni,val_nj))
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j]==val_bg: g[val_i][val_j]=3
            elif g[val_i][val_j]==-1: g[val_i][val_j]=val_bg
    return g
