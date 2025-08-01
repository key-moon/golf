def p(g):
    val_c=[];val_h=len(g);val_w=len(g[0])
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j]==8:
                val_l=[val_i,val_j];g[val_i][val_j]=0;val_p=0
                while val_p<len(val_l):
                    val_y,val_x=val_l[val_p],val_l[val_p+1];val_p+=2
                    for val_a,val_b in((1,0),(-1,0),(0,1),(0,-1)):
                        val_ny,val_nx=val_y+val_a,val_x+val_b
                        if 0<=val_ny<val_h and 0<=val_nx<val_w and g[val_ny][val_nx]==8:
                            g[val_ny][val_nx]=0; val_l+= [val_ny,val_nx]
                val_c.append(val_l)
    val_c.sort(key=len)
    # largest component → color 1, smallest → color 2
    for val_y,val_x in zip(val_c[-1][::2],val_c[-1][1::2]): g[val_y][val_x]=1
    for val_y,val_x in zip(val_c[ 0][::2],val_c[ 0][1::2]): g[val_y][val_x]=2
    return g
