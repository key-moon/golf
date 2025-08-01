def p(g):
    val_h,val_w=len(g),len(g[0])
    val_s=[]
    # collect all straight segments of 4s
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j]==4:
                # horizontal
                if val_j==0 or g[val_i][val_j-1]!=4:
                    val_l=1
                    while val_j+val_l<val_w and g[val_i][val_j+val_l]==4:
                        val_l+=1
                    if val_l>1:
                        val_s.append((val_i,val_j,0,1,val_l))
                # vertical
                if val_i==0 or g[val_i-1][val_j]!=4:
                    val_l=1
                    while val_i+val_l<val_h and g[val_i+val_l][val_j]==4:
                        val_l+=1
                    if val_l>1:
                        val_s.append((val_i,val_j,1,0,val_l))
    # look for any two segments that match in orientation & length
    for a in range(len(val_s)):
        for b in range(a+1,len(val_s)):
            i1,j1,di,dj,L=val_s[a]
            i2,j2,di2,dj2,L2=val_s[b]
            if di==di2 and dj==dj2 and L==L2:
                # reflect any colored cell adjacent to seg a across to seg b
                for r in range(val_h):
                    for c in range(val_w):
                        v=g[r][c]
                        if v and v!=4:
                            rr,cc=r-i1,c-j1
                            a0=rr*di+cc*dj
                            if 0<=a0<L:
                                dr,dc=rr-a0*di,cc-a0*dj
                                # perpendicular outward of segment a?
                                if (dr,dc)==( dj,-di):
                                    g[i2+a0*di-dj][j2+a0*dj+di]=v
                                if (dr,dc)==(-dj, di):
                                    g[i2+a0*di+dj][j2+a0*dj-di]=v
                return g
    return g
