def p(g):
 s=[*map(list,g)];D=-1,0,1;E=[(i,j)for i in D for j in D if i|j]
 for a in range(len(g)-1):
  for b in range(len(g[0])-1):
   if len(set(V:=g[a][b:b+2]+g[a+1][b:b+2]))<4:continue
   for t in 0,1,2,3:
    x=a+(t>1);y=b+(t&1)
    if(k:=V[t])and any(g[x+i][y+j]==k for i,j in E):
     A=a+a+1;B=b+b+1;q=[(x,y)];g[x][y]=0
     while q:
      x,y=q.pop()
      for u in 0,1,2,3:s[(x,A-x)[(u>>1)!=(x>a)]][(y,B-y)[(u&1)!=(y>b)]]=V[u]
      for i,j in E:
       u=x+i;v=y+j
       try:
        if g[u][v]==k:g[u][v]=0;q+=[(u,v)]
       except:0
     break
 return s