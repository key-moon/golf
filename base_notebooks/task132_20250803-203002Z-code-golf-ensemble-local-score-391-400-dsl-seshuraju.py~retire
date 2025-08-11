def p(g):
 H, W=len(g), len(g[0])
 res=[[0]*W for _ in range(H)]
 colors={v for row in g for v in row if v}
 for c in colors:
     ys=[i for i,row in enumerate(g)for v in row if v==c]
     xs=[j for i,row in enumerate(g)for j,v in enumerate(row)if v==c]
     y0,y1=min(ys), max(ys)+1
     x0,x1=min(xs), max(xs)+1
     for i in range(y0,y1):
         for j in range(x0,x1):
             res[i][j]=c
 return res