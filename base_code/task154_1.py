def p(g):
 R,C=len(g),len(g[0])
 S=lambda v: [(i,j) for i in range(R) for j in range(C) if g[i][j]==v]
 a=S(2)
 r0,r1=min(i for i,_ in a),max(i for i,_ in a)
 c0,c1=min(j for _,j in a),max(j for _,j in a)
 vis=[[0]*C for _ in g]
 o=[[0]*C for _ in g]
 for i,j in a: o[i][j]=2
 for i,j in S(5):
  if not vis[i][j]:
    Q=[(i,j)];comp=[]
    for x,y in Q:
      if not vis[x][y]:
        vis[x][y]=1; comp.append((x,y))
        for xx,yy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
          if 0<=xx<R and 0<=yy<C and g[xx][yy]==5 and not vis[xx][yy]:
            Q.append((xx,yy))
    rs=[x for x,_ in comp]; cs=[y for _,y in comp]
    H,W=max(rs)-min(rs)+1,max(cs)-min(cs)+1
    above=max(rs)<r0
    if W==1:           # vertical bar
      nr = (r0+2) if above else (r1-2-H+1)
      nc=cs[0]
      for k in range(H): o[nr+k][nc]=5
 else
      nr = (r0+2) if above else (r1-2)
      for x,y in comp: o[nr][y]=5
 return o
