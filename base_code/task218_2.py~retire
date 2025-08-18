def p(g):
 val_h,val_w=len(g),len(g[0])
 val_xs=sorted({0,val_w}|{i+1 for i in range(val_w-1)if any(g[y][i]!=g[y][i+1]for y in range(val_h))})
 val_ys=sorted({0,val_h}|{i+1 for i in range(val_h-1)if any(g[i][x]!=g[i+1][x]for x in range(val_w))})
 val_m=[[g[(val_ys[i]+val_ys[i+1]-1)//2][(val_xs[j]+val_xs[j+1]-1)//2]
         for j in range(len(val_xs)-1)]for i in range(len(val_ys)-1)]
 val_m=[r for r in val_m if any(r)]
 val_t=zip(*val_m);val_t=[r for r in val_t if any(r)]
 return list(map(list,zip(*val_t)))
