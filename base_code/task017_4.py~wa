def p(g):
    val_R=len(g);val_C=len(g[0])
    for val_h in range(1,val_R+1):
        if val_R%val_h:continue
        for val_w in range(1,val_C+1):
            if val_C%val_w:continue
            val_ok=1
            for val_i in range(val_R):
                for val_j in range(val_C):
                    if g[val_i][val_j] and g[val_i][val_j]!=g[val_i%val_h][val_j%val_w]:
                        val_ok=0;break
                if not val_ok:break
            if val_ok:break
        if val_ok:break
    for val_i in range(val_R):
        for val_j in range(val_C):
            if not g[val_i][val_j]:
                g[val_i][val_j]=g[val_i%val_h][val_j%val_w]
    return g
