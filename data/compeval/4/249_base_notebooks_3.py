def p(g):
 ry, rx = 1, 2
 h, w = len(g), len(g[0])
 return [[g[i % h][j % w] for j in range(w * rx)]
         for i in range(h * ry)]