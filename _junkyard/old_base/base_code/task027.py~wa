def p(g):
 h,w=len(g),len(g[0])
 v=[[0]*w for _ in g]
 st=[]
 # collect all border‐zeros
 for i,j in [(0,y) for y in range(w)]+[(h-1,y) for y in range(w)]+[(x,0) for x in range(h)]+[(x,w-1) for x in range(h)]:
  if g[i][j]==0:
   v[i][j]=1
   st.append((i,j))
 # mark background zeros
 while st:
  x,y=st.pop()
  for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
   i,j=x+dx,y+dy
   if 0<=i<h and 0<=j<w and not v[i][j] and g[i][j]==0:
    v[i][j]=1
    st.append((i,j))
 # fill holes
 for i in range(h):
  for j in range(w):
   if g[i][j]==0 and not v[i][j]:
    g[i][j]=2
 return g
