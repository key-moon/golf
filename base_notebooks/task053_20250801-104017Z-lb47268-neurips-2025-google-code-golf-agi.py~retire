def p(g):
 H, W = len(g), len(g[0])
 ys = [i for i,row in enumerate(g) for v in row if v]
 xs = [j for i,row in enumerate(g) for j,v in enumerate(row) if v]
 res = [[0]*W for _ in range(H)]
 for i,j in zip(ys, xs):
     ni, nj = i+1, j+0
     if 0 <= ni < H and 0 <= nj < W:
         res[ni][nj] = g[i][j]
 return res
