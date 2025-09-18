def p(g):
 val_v=[(i,j)for i,row in enumerate(g)for j,c in enumerate(row)if c==5]
 val_s=sum(i for i,_ in val_v);val_t=sum(j for _,j in val_v);val_l=len(val_v)
 for val_i,val_j in val_v:g[val_i][val_j]=8 if(val_i*val_l-val_s)*(val_j*val_l-val_t)>0 else 2
 return g
