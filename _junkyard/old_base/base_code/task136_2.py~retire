def p(g):
    val_n=len(g)
    val_vs=sorted({g[i][j] for i in range(val_n) for j in range(val_n) if g[i][j]})
    for val_c in val_vs:
        val_p=[(i,j) for i in range(val_n) for j in range(val_n) if g[i][j]==val_c]
        val_I,val_J=zip(*val_p)
        val_a,val_e=min(val_I),max(val_I)
        val_b,val_d=min(val_J),max(val_J)
        if val_c==val_vs[0]:
            val_i,val_j=val_a,val_b
            while val_i and val_j:
                val_i-=1; val_j-=1
                g[val_i][val_j]=val_c
        else:
            val_i,val_j=val_e,val_d
            while val_i<val_n-1 and val_j<val_n-1:
                val_i+=1; val_j+=1
                g[val_i][val_j]=val_c
    return g
