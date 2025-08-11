def p(g):
    val_s=len({c for r in g for c in r if c});val_n=len(g)*val_s
    return[
        [g[y//val_s][x//val_s] or ((y==x or x+y==val_n-1) and 2)
            for x in range(val_n)
        ]
        for y in range(val_n)
    ]
