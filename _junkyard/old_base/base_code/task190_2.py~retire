def p(g):
    val_n=len(g)
    val_br,val_bc=next((val_i,val_j) for val_i in range(val_n-1) for val_j in range(val_n-1) if g[val_i][val_j] and g[val_i][val_j]==g[val_i][val_j+1]==g[val_i+1][val_j]==g[val_i+1][val_j+1])
    val_x=g[val_br][val_bc]
    for val_i in range(val_n):
        for val_j in range(val_n):
            if g[val_i][val_j]==val_x and not(val_br<=val_i<=val_br+1 and val_bc<=val_j<=val_bc+1):
                val_dr=1 if val_i>val_br else -1
                val_dc=1 if val_j>val_bc else -1
                val_k=1
                while 0<=val_i+val_k*val_dr<val_n and 0<=val_j+val_k*val_dc<val_n:
                    g[val_i+val_k*val_dr][val_j+val_k*val_dc]=val_x
                    val_k+=1
    return g
