def p(g):
 r,c=len(g),len(g[0]);s=set()
 for i in range(r):
  for j in range(c):
   v=g[i][j]
   if v:
    if i+1<r and (w:=g[i+1][j])!=v and w:s|={v,w}
    if j+1<c and (w:=g[i][j+1])!=v and w:s|={v,w}
 d=[(i,j)for i in range(r)for j in range(c)if g[i][j]in s]
 a=min(i for i,_ in d);b=max(i for i,_ in d)
 e=min(j for _,j in d);f=max(j for _,j in d)
 P=[g[i][e:f+1]for i in range(a,b+1)]
 h,w=len(P),len(P[0])
 q={v for R in g for v in R if v and v not in s}
 for i in range(r-h+1):
  for j in range(c-w+1):
   v=g[i][j]
   if v in q and (i==0 or g[i-1][j]!=v)and(j==0 or g[i][j-1]!=v)and all(g[i+u][j:j+w]==[v]*w for u in range(h)):
    for u in range(h):
     for k in range(w):
      g[i+u][j+k]=P[u][k]
 return g
