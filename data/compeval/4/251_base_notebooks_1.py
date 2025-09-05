def p(g):
     h,w=len(g),len(g[0])
     v=[[0]*w for _ in range(h)]
     q=[]
     for i in range(h):
      for j in range(w):
       if i*j==0 or i==h-1 or j==w-1:
        if g[i][j]==0:v[i][j]=1;q.append((i,j))
     while q:
      r,c=q.pop(0)
      for dr,dc in[(-1,0),(1,0),(0,-1),(0,1)]:
       nr,nc=r+dr,c+dc
       if 0<=nr<h and 0<=nc<w and g[nr][nc]==0 and not v[nr][nc]:
        v[nr][nc]=1;q.append((nr,nc))
     res=[[g[i][j]if g[i][j]!=0 or v[i][j]else 1 for j in range(w)]for i in range(h)]
     return res
