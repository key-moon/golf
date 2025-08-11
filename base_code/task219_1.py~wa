def p(g):
 for val_b,val_o in ((5,1),(10,2)):
  val_rows=[i for i in range(val_b,val_b+5) if any(g[i][j]==8 for j in range(10))]
  if not val_rows: continue
  val_r=val_rows[-1]+val_o
  for j in range(10):
   if any(g[i][j]==8 for i in range(5)) and all(g[i][j]!=8 for i in range(val_b,val_b+5)):
    g[val_r][j]=1
 return g
