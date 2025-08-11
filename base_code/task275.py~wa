def p(g):
    h,w=len(g),len(g[0])
    k=min(h,w);n=k*k
    o=[[0]*n for _ in[0]*n]
    for i in range(k):
      for j in range(k):
        v=g[i][j]
        if v:
          x=i*k+k//2; y=j*k+k//2
          for d in range(n):
            if d//k==i or d%k==j:
              o[d//k*k+k//2][d%k*k+k//2]=v
    return o
