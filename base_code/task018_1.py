def p(g):
 val_r,val_c=len(g),len(g[0])
 val_G=[row[:]for row in g]
 val_v=[[0]*val_c for _ in range(val_r)]
 val_d=[(1,0),(-1,0),(0,1),(0,-1)]
 val_comps=[]
 for val_i in range(val_r):
  for val_j in range(val_c):
   if g[val_i][val_j] and not val_v[val_i][val_j]:
    val_st=[(val_i,val_j)]
    val_v[val_i][val_j]=1
    for val_y,val_x in val_st:
     for dy,dx in val_d:
      ny, nx = val_y+dy, val_x+dx
      if 0<=ny<val_r and 0<=nx<val_c and g[ny][nx] and not val_v[ny][nx]:
       val_v[ny][nx]=1
       val_st.append((ny,nx))
    b0,b1=val_st[0]
    val_shape=tuple(sorted(((y-b0,x-b1,g[y][x]) for y,x in val_st)))
    val_comps.append((val_shape,val_st,b0,b1))
 val_cnt={}
 for s,st,_,_ in val_comps: val_cnt[s]=val_cnt.get(s,0)+1
 for s,st,_,_ in val_comps:
  if val_cnt[s]==2:
   val_block=s
   val_twice=[x for x in val_comps if x[0]==s]
   break
 # erase both occurrences
 for _,st,_,_ in val_twice:
  for y,x in st: val_G[y][x]=0
 # bounding box of the block
 dys=[dy for dy,dx,v in val_block]; dxs=[dx for dy,dx,v in val_block]
 H=max(dys)-min(dys)+1; W=max(dxs)-min(dxs)+1
 # find the one place it fits
 for ii in range(val_r-H+1):
  for jj in range(val_c-W+1):
   if all(val_G[ii+dy][jj+dx]==0 for dy,dx,v in val_block):
    for dy,dx,v in val_block: val_G[ii+dy][jj+dx]=v
    return val_G
