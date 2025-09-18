def p(g):
    # dims
    val_h,val_w=len(g),len(g[0])
    # background is the most frequent color
    vals=[c for r in g for c in r]
    val_BG=max(set(vals),key=vals.count)
    # mark & collect all non‐BG components
    val_vis=[[0]*val_w for _ in range(val_h)]
    val_comps=[]
    for i in range(val_h):
        for j in range(val_w):
            if g[i][j]!=val_BG and not val_vis[i][j]:
                val_stack=[(i,j)];val_vis[i][j]=1;val_comp=[]
                while val_stack:
                    x,y=val_stack.pop();val_comp.append((x,y))
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        u,v=x+dx,y+dy
                        if 0<=u<val_h and 0<=v<val_w and not val_vis[u][v] and g[u][v]!=val_BG:
                            val_vis[u][v]=1;val_stack.append((u,v))
                val_comps.append(val_comp)
    # pick the one comp whose colors>1 ⇒ our motif
    for val_comp in val_comps:
        val_cols={g[x][y] for x,y in val_comp}
        if len(val_cols)>1:
            break
    # bbox of motif
    val_rs=[x for x,y in val_comp];val_cs=[y for x,y in val_comp]
    val_r0,val_c0=min(val_rs),min(val_cs)
    # record shape = (dr,dc,color)
    val_shape=[(x-val_r0,y-val_c0,g[x][y]) for x,y in val_comp]
    # group shape‐cells by their color ⇒ seeds
    val_seeds={}
    for dr,dc,v in val_shape:
        val_seeds.setdefault(v,[]).append((dr,dc))
    # for each seed‐color, stamp motif at every OTHER occurrence of that color
    for v,pts in val_seeds.items():
        # within motif, the “origin” offset for this color is its minimal (dr,dc)
        od=min(pts)
        odx,ody=od
        for i in range(val_h):
            for j in range(val_w):
                if g[i][j]==v and (i-val_r0,j-val_c0,v) not in val_shape:
                    # compute placement origin
                    Dx,Ky=i-odx,j-ody
                    # paint every cell of motif
                    for dr,dc,w in val_shape:
                        g[Dx+dr][Ky+dc]=w
    return g
