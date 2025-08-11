def p(g):
    for i in range(len(g)-6):
        for j in range(len(g[0])-6):
            v=g[i][j]
            if g[i][j:j+7]==[v]*7==g[i+6][j:j+7] and all(g[i+k][j:j+7:6]==[v,v] for k in range(7)):
                return [r[j:j+7] for r in g[i:i+7]]
