def p(g):
 val_o=[[0]*len(g[0])for _ in g];val_H,val_W=len(g),len(g[0])
 for val_y in range(val_H):
  for val_x in range(val_W):
   val_c=g[val_y][val_x]
   if val_c and (val_y<1 or g[val_y-1][val_x]!=val_c) and (val_x<1 or g[val_y][val_x-1]!=val_c):
    val_w=1
    while val_x+val_w<val_W and g[val_y][val_x+val_w]==val_c:val_w+=1
    val_h=1
    while val_y+val_h<val_H and g[val_y+val_h][val_x]==val_c:val_h+=1
    if val_w>1 and val_h>1 and all(g[val_y+i][val_x+j]==val_c for i in range(val_h) for j in range(val_w)):
     for i in range(val_h):
      for j in range(val_w):val_o[val_y+i][val_x+j]=val_c
 return val_o
