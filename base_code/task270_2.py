def p(g):
    val_D={}
    for val_i,val_r in enumerate(g):
        for val_j,val_v in enumerate(val_r):
            val_v and val_D.setdefault(val_v,[]).append((val_i,val_j))
    val_cs=sorted([c for c,s in val_D.items() if len(s)==1])
    val_ss=sorted([s for s,s2 in val_D.items() if len(s2)==4],reverse=1)
    val_o=[[0]*len(g[0])for _ in g]
    for val_s,val_c in zip(val_ss,val_cs):
        val_ps=val_D[val_s]
        val_rs=[i for i,j in val_ps]; val_cs2=[j for i,j in val_ps]
        val_x=[v for v in set(val_rs) if val_rs.count(v)==2][0]
        val_y=[v for v in set(val_cs2) if val_cs2.count(v)==2][0]
        val_o[val_x][val_y]=val_c
        for val_dx,val_dy in((1,0),(-1,0),(0,1),(0,-1)):
            val_o[val_x+val_dx][val_y+val_dy]=val_s
    return val_o