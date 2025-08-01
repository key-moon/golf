def p(val_g):
    return [8,0][sum(val_i+val_j
        for val_i in range(len(val_g)-1)
        for val_j in range(len(val_g[0])-1)
        if val_g[val_i][val_j]==2==val_g[val_i][val_j+1]==val_g[val_i+1][val_j]==val_g[val_i+1][val_j+1]
    )%2]
