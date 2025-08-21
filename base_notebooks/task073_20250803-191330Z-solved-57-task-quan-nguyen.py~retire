def p(g):
     h,w=len(g),len(g[0])
     r=[[0]*w for _ in range(h)]
     for c in range(w):
      for i in range(h):
       v=g[i][c]
       if v not in[0,5]:
        for j in range(h-1,-1,-1):
         if g[j][c]==5:r[j][c]=v;break
        break
      for i in range(h):
       if g[i][c]==5 and r[i][c]==0:r[i][c]=5
     return r