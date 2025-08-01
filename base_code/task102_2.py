def p(val_g):
    val_h,val_w=len(val_g),len(val_g[0])
    for val_x in range(val_h):
        for val_y in range(val_w):
            if val_g[val_x][val_y]==5:
                for val_k in range(3,min(val_h-val_x,val_w-val_y)+1):
                    if all(
                        val_g[val_x][val_y+i]==5 and
                        val_g[val_x+val_k-1][val_y+i]==5 and
                        val_g[val_x+i][val_y]==5 and
                        val_g[val_x+i][val_y+val_k-1]==5
                        for i in range(val_k)
                    ):
                        for val_i in range(1,val_k-1):
                            for val_j in range(1,val_k-1):
                                if val_g[val_x+val_i][val_y+val_j]==0:
                                    val_g[val_x+val_i][val_y+val_j]=2
    return val_g
