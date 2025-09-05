def p(g):
 val_r=next(i for i,x in enumerate(g)if len({*x})<2)
 val_c=next(j for j in range(len(g[0]))if len({g[i][j]for i in range(len(g))})<2)
 val_a=[[g[i][j]for j in range(len(g[0]))if j!=val_c]for i in range(len(g))if i!=val_r]
 val_f=[x for r in val_a for x in r]
 val_b=max({*val_f},key=val_f.count)
 val_i,val_j=next((i,j)for i,r in enumerate(val_a)for j,x in enumerate(r)if x!=val_b)
 return [r[:val_c]if val_j<val_c else r[val_c:]for r in(val_a[:val_r]if val_i<val_r else val_a[val_r:])]
