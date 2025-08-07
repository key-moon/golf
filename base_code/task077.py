def p(g):
 for val_i,val_row in enumerate(g):
  for val_j,val_v in enumerate(val_row):
   if val_v*(val_v-2):
    try:
     if g[val_i+1][val_j]==2 or g[val_i-1][val_j]==2 or val_row[val_j+1]==2 or val_row[val_j-1]==2:val_row[val_j]=4
    except:pass
 return g
