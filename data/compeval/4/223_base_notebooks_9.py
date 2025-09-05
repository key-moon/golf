def p(g):
 H, W = len(g), len(g[0])
 ky, kx = 3, 3
 return [[ g[i//ky][j//kx] for j in range(W*kx) ] for i in range(H*ky)]