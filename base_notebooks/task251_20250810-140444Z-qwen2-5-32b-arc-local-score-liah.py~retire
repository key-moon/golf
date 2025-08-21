def p(g,V=range):
     h,w=len(g),len(g[0])
     v=[[0]*w for _ in V(h)]
     q=[]
     for i in V(h):
      for j in V(w):
       if i*j==0 or i==h-1 or j==w-1:
        if g[i][j]==0:v[i][j]=1;q.append((i,j))
     while q:
      r,c=q.pop(0)
      for d,k in[(-1,0),(1,0),(0,-1),(0,1)]:
       F,a=r+d,c+k
       if 0<=F<h and 0<=a<w and g[F][a]==0 and not v[F][a]:v[F][a]=1;q.append((F,a))
     L=[[g[i][j]if g[i][j]!=0 or v[i][j]else 1 for j in V(w)]for i in V(h)]
     return L