def p(g):
    for val_i in range(len(g)-2):
        for val_j in range(len(g)-2):
            if sum(g[val_i+val_u][val_j+val_v]==4 for val_u in range(3) for val_v in range(3))==6:
                for val_u in range(3):
                    for val_v in range(3):
                        if not g[val_i+val_u][val_j+val_v]:
                            g[val_i+val_u][val_j+val_v]=7
    return g
