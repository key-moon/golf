def p(g):
 val_bs=[vj for vj,vc in enumerate(zip(*g)) if len({*vc})==1 and vc[0]]
 val_c1,val_c2=val_bs
 val_rs=[ri for ri,row in enumerate(g) if len({*row[val_c1+1:val_c2]})==1 and row[val_c1+1]]
 val_a,val_b=val_rs[0],val_rs[-1]
 return [r[val_c1:val_c2+1] for r in g[val_a:val_b+1]]
