def p(g):
    val_v0=g[0]
    while 1:
        # find a 5
        for val_t in range(100):
            if g[val_t//10][val_t%10]==5:
                val_a=[val_t]
                g[val_t//10][val_t%10]=0
                break
        else:
            break
        # flood‐fill into val_a
        for val_p in val_a:
            if val_p%10<9 and g[val_p//10][val_p%10+1]==5:
                val_a+=val_p+1; g[val_p//10][val_p%10+1]=0
            if val_p%10>0 and g[val_p//10][val_p%10-1]==5:
                val_a+=val_p-1; g[val_p//10][val_p%10-1]=0
            if val_p//10<9 and g[val_p//10+1][val_p%10]==5:
                val_a+=val_p+10; g[val_p//10+1][val_p%10]=0
            if val_p//10>0 and g[val_p//10-1][val_p%10]==5:
                val_a+=val_p-10;g[val_p//10-1][val_p%10]=0
        # determine the replacement colour
        val_c=next(val_v0[val_k]
                    for val_k in range(
                              min(val_p%10 for val_p in val_a),
                              max(val_p%10 for val_p in val_a)+1
                            )
                    if val_v0[val_k])
        # paint the cluster
        for val_p in val_a:
            g[val_p//10][val_p%10]=val_c
    return g
