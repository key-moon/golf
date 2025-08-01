def p(g):
 val_n,len_=len(g),len
 val_m=len_(g[0])
 val_y=val_x=val_i=0
 val_d=[(0,1),(1,0),(0,-1),(-1,0)]
 while 1:
  val_l=(val_m if val_i%2<1 else val_n-1)-2*(val_i//2)
  if val_l<1: break
  dy,dx=val_d[val_i%4]
  for _ in range(val_l):
   g[val_y][val_x]=3
   val_y+=dy*(_<val_l-1); val_x+=dx*(_<val_l-1)
  val_i+=1
 return g
