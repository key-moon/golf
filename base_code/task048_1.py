def p(g):
    return [8,0][sum(val_i+val_j
        for val_i in range(len(g)-1)
        for val_j in range(len(g[0])-1)
        if g[val_i][val_j]==2==g[val_i][val_j+1]==g[val_i+1][val_j]==g[val_i+1][val_j+1]
    )%2]
