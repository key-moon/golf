def p(g):
 for val_r,val_row in enumerate(g):
  if val_row.count(8)==len(val_row):break
 for val_c,val_col in enumerate(zip(*g)):
  if val_col.count(8)==len(val_col):break
 val_L=[[r[:val_c]     for r in g[:val_r]],[r[val_c+1:]   for r in g[:val_r]],[r[:val_c]     for r in g[val_r+1:]],[r[val_c+1:]   for r in g[val_r+1:]]]
 val_v=next(x for x in val_L if len(x)==2 and len(x[0])==2)
 val_m=next(x for x in val_L if len(x)>2 and len(x[0])>2)
 val_h,val_w=len(val_m),len(val_m[0])
 val_bh,val_bw=val_h//2,val_w//2
 return [[val_m[i][j]//3*val_v[i//val_bh][j//val_bw] for j in range(val_w)]for i in range(val_h)]
