def p(g):
 val_v=sorted(j for j in range(len(g[0]))if len({g[i][j]for i in range(len(g))})==1)
 val_a,val_b=val_v
 val_r=[i for i in range(len(g))if len({g[i][j]for j in range(val_a+1,val_b)})==1]
 return[row[val_a:val_b+1]for row in g[val_r[0]:val_r[-1]+1]]
