def p(g):
    val_n,len0=len(g),len(g[0])
    val_m=len0
    val_B=[[0]*val_m for _ in range(val_n)]
    for val_r in range(val_n-1):
        for val_c in range(val_m-1):
            val_A=[g[val_r+vi][val_c+vj] for vi in(0,1) for vj in(0,1)]
            if val_A.count(2)==1 and (S:=set(val_A)-{2}):
                val_v=S.pop()
                val_k=val_A.index(2)
                val_i,val_j=divmod(val_k,2)
                val_dr=-1 if val_i<1 else 1
                val_dc=-1 if val_j<1 else 1
                val_pr=[-val_dc,val_dr]
                val_x,val_y=val_r+val_i,val_c+val_j
                while 0<=val_x<val_n and 0<=val_y<val_m:
                    for val_t in(-1,0,1):
                        val_xx,val_yy=val_x+val_pr[0]*val_t,val_y+val_pr[1]*val_t
                        if 0<=val_xx<val_n and 0<=val_yy<val_m:
                            val_B[val_xx][val_yy]=val_v
                    val_x+=val_dr;val_y+=val_dc
                return val_B
