def p(g):
     h, w = len(g), len(g[0])
     ys = [i for i, row in enumerate(g) for v in row if v]
     xs = [j for i, row in enumerate(g) for j, v in enumerate(row) if v]
     res = [[0]*w for _ in range(h)]
     for i, j in zip(ys, xs):
         ni, nj = i + 1, j + 0
         if 0 <= ni < h and 0 <= nj < w:
             res[ni][nj] = g[i][j]
     return res
    