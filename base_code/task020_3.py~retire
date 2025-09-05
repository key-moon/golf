def p(g):
    val_H=len(g)
    val_pts=[(i,j,g[i][j]) for i in range(val_H) for j in range(val_H) if g[i][j]]
    val_pr=(min(i[0] for i in val_pts)+max(i[0] for i in val_pts))//2
    val_pc=(min(j[1] for j in val_pts)+max(j[1] for j in val_pts))//2
    for val_i,val_j,val_v in val_pts:
        g[val_pr-(val_j-val_pc)][val_pc+(val_i-val_pr)]=val_v
        g[2*val_pr-val_i][2*val_pc-val_j]=val_v
        g[val_pr+(val_j-val_pc)][val_pc-(val_i-val_pr)]=val_v
    return g
