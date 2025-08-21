def p(g):
 H=len(g);W=len(g[0]);v=[[0]*W for _ in range(H)];B=[];C=0
 for i in range(H):
  for j in range(W):
   c=g[i][j]
   if c and not v[i][j]:
    q=[(i,j)];v[i][j]=1;S=[(i,j)]
    while q:
     x,y=q.pop()
     for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      a,b=x+dx,y+dy
      if 0<=a<H and 0<=b<W and not v[a][b] and g[a][b]==c:
       v[a][b]=1;q.append((a,b));S.append((a,b))
    if len(S)>len(B):B=S;C=c
 if not B:return[[]]
 R=[i for i,_ in B];K=[j for _,j in B]
 t,b=min(R),max(R);l,r=min(K),max(K);S=set(B)
 return[[C if (t+x,l+y) in S else 0 for y in range(r-l+1)]for x in range(b-t+1)]