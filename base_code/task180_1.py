def p(g):return[[g[val_i][val_j+4]or g[val_i+4][val_j]or g[val_i][val_j]or g[val_i+4][val_j+4]for val_j in range(4)]for val_i in range(4)]
