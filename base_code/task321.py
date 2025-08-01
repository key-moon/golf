def p(g):
    a = g[0].index(2)
    b = g[0].index(2, a+1)
    return [
        [x or y or z
         for x,y,z in zip(r[:a], r[a+1:b], r[b+1:])]
        for r in g
    ]
