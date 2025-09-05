def p(g):
 R=range
 b,v=[],set()
 for i in R(10):
  for j in R(10):
   if g[i][j]and(i,j)not in v:
    r=j
    while r<10and g[i][r]:r+=1
    r-=1
    t=i
    while t<10and all(g[t][k]for k in R(j,r+1)):t+=1
    t-=1
    k=[[g[u][w]for w in R(j,r+1)]for u in R(i,t+1)]
    for u in R(i,t+1):
     for w in R(j,r+1):v.add((u,w))
    b.append((sum(sum(x==2for x in row)for row in k),k))
 return max(b)[1]