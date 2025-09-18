def p(g):
 val_h,val_w=len(g),len(g[0]);val_s=[[0]*val_w for _ in g]
 for val_i in range(val_h):
  for val_j in range(val_w):
   if g[val_i][val_j] and not val_s[val_i][val_j]:
    val_c=g[val_i][val_j];val_st=[(val_i,val_j)];val_s[val_i][val_j]=1;val_pts=[]
    while val_st:
     x,y=val_st.pop();val_pts.append((x,y))
     for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      nx,ny=x+dx,y+dy
      if 0<=nx<val_h and 0<=ny<val_w and not val_s[nx][ny] and g[nx][ny]==val_c:
       val_s[nx][ny]=1;val_st.append((nx,ny))
    val_rs=[p[0]for p in val_pts];val_cs=[p[1]for p in val_pts]
    r0,r1,c0,c1=min(val_rs),max(val_rs),min(val_cs),max(val_cs)
    if r1-r0>1 and c1-c0>1 and all(g[r0][k]==val_c for k in range(c0,c1+1)) and all(g[r1][k]==val_c for k in range(c0,c1+1)) and all(g[k][c0]==val_c for k in range(r0,r1+1)) and all(g[k][c1]==val_c for k in range(r0,r1+1)):
      for x in range(r0+1,r1):
       for y in range(c0+1,c1):g[x][y]=2
 return g
