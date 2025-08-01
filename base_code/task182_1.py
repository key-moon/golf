def p(g):
    val_h,val_w=len(g),len(g[0])
    # all nonzero colours and their counts
    val_vals={c for r in g for c in r if c}
    val_cnt={c:sum(r.count(c)for r in g)for c in val_vals}
    # ring‐border is the most frequent, interior is the least
    val_B,val_Y=max(val_cnt,key=val_cnt.get),min(val_cnt,key=val_cnt.get)
    # bounding‐box of ring
    val_minr=min(i for i,R in enumerate(g)for j,v in enumerate(R)if v==val_B)
    val_maxr=max(i for i,R in enumerate(g)for j,v in enumerate(R)if v==val_B)
    val_minc=min(j for R in g    for j,v in enumerate(R)if v==val_B)
    val_maxc=max(j for R in g    for j,v in enumerate(R)if v==val_B)
    # interior box is one in
    val_r0,val_r1,val_c0,val_c1=val_minr+1,val_maxr,val_minc+1,val_maxc
    # mask of the little shape inside the ring
    val_mask=[(i-val_r0,j-val_c0)
              for i in range(val_r0,val_r1)
              for j in range(val_c0,val_c1)
              if g[i][j]==val_Y]
    val_h2,val_w2=val_r1-val_r0,val_c1-val_c0
    # pick the “external” colour(s) to search for
    val_ext=[c for c in val_vals if c not in (val_B,val_Y)]
    val_X=val_ext[0] if val_ext else None
    # flood‐fill each component of colour X and if its shape matches the mask, repaint it
    val_vis=set()
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j]==val_X and (val_i,val_j) not in val_vis:
                val_st=[(val_i,val_j)];val_comp=[]
                val_vis.add((val_i,val_j))
                while val_st:
                    val_a,val_b=val_st.pop();val_comp.append((val_a,val_b))
                    for val_di,val_dj in((1,0),(-1,0),(0,1),(0,-1)):
                        val_ni,val_nj=val_a+val_di,val_b+val_dj
                        if (0<=val_ni<val_h and 0<=val_nj<val_w
                            and g[val_ni][val_nj]==val_X
                            and (val_ni,val_nj) not in val_vis):
                            val_vis.add((val_ni,val_nj))
                            val_st.append((val_ni,val_nj))
                mi0,mi1=min(a for a,b in val_comp),max(a for a,b in val_comp)
                mj0,mj1=min(b for a,b in val_comp),max(b for a,b in val_comp)
                if (mi1-mi0+1==val_h2 and mj1-mj0+1==val_w2
                    and set((a-mi0,b-mj0) for a,b in val_comp)==set(val_mask)):
                    for val_a,val_b in val_comp:
                        g[val_a][val_b]=val_Y
    return g
