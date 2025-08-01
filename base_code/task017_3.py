def p(g):
    val_H,val_W=len(g),len(g[0])
    for val_h in range(1,val_H):
        for val_r in range(val_H-val_h):
            for val_c in range(val_W):
                if g[val_r][val_c] and g[val_r+val_h][val_c] and g[val_r][val_c]!=g[val_r+val_h][val_c]:
                    break
         else
            break
     else
    for val_w in range(1,val_W):
        for val_r in range(val_H):
            for val_c in range(val_W-val_w):
                if g[val_r][val_c] and g[val_r][val_c+val_w] and g[val_r][val_c]!=g[val_r][val_c+val_w]:
                    break
         else
            break
     else
    for val_r in range(val_H):
        for val_c in range(val_W):
            if not g[val_r][val_c]:
                g[val_r][val_c]=g[val_r%val_h][val_c%val_w]
    return g
