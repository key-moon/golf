def p(g):
    val_h,val_w=len(g),len(g[0]);val_vs=[[0]*val_w for _ in g]
    val_br=[];val_bl=[]
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j] and not val_vs[val_i][val_j]:
                val_c=g[val_i][val_j]
                val_q=[(val_i,val_j)];val_vs[val_i][val_j]=1;val_L=[]
                while val_q:
                    val_x,val_y=val_q.pop();val_L.append((val_x,val_y))
                    for val_u,val_v in((val_x+1,val_y),(val_x-1,val_y),(val_x,val_y+1),(val_x,val_y-1)):
                        if 0<=val_u<val_h and 0<=val_v<val_w and not val_vs[val_u][val_v] and g[val_u][val_v]==val_c:
                            val_vs[val_u][val_v]=1;val_q.append((val_u,val_v))
                val_rs,val_cs=zip(*val_L)
                val_r0,val_r1,minC,maxC=min(val_rs),max(val_rs),min(val_cs),max(val_cs)
                val_q2=(val_r0+val_r1<val_h)+(minC+maxC<val_w)*2
                if val_c==5:
                    val_br.append((val_q2,val_r0,val_r1,minC,maxC))
                else:
                    val_bl.append((val_q2,val_r0,val_r1,minC,maxC,val_c,val_L))
    for val_q2,val_r0,val_r1,val_c0,val_c1 in val_br:
        for _,val_r0b,val_r1b,val_c0b,val_c1b,val_d,val_L2 in val_bl:
            if val_q2==_:
                for val_x,val_y in val_L2: g[val_x][val_y]=0
                val_sr=val_r0+1 if val_q2<2 else val_r1-2
                val_sc=val_c0+1 if val_q2%2==0 else val_c1-2
                for val_dx in(0,1):
                    for val_dy in(0,1):
                        g[val_sr+val_dx][val_sc+val_dy]=val_d
    return g
