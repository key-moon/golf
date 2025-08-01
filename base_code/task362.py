def p(g):
    k = sum(x == 5 for r in g for x in r)
    c = next(x for r in g for x in r if x % 5)
    n = len(g); m = len(g[0])
    return [
        [c if 0 <= i - k < n and 0 <= j + k < m and g[i - k][j + k] == c else 0
         for j in range(m)]
        for i in range(n)
    ]
