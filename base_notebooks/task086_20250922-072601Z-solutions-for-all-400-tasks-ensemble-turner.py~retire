def p(a):
 from collections import deque,Counter
 R,L=range,len;n,m=L(a),L(a[0]);o=[[0]*m for _ in R(n)];v=[[0]*m for _ in R(n)]
 for i in R(n):
  for j in R(m):
   if a[i][j]and not v[i][j]:
    q=deque([(i,j)]);v[i][j]=1;P=[];c=Counter()
    while q:
     r,x=q.popleft();P.append((r,x));c[a[r][x]]+=1
     for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
      y,z=r+dr,x+dc
      if 0<=y<n and 0<=z<m and a[y][z]and not v[y][z]:v[y][z]=1;q.append((y,z))
    oc,ic=[k for k,_ in c.most_common(2)];S=[(r,x)for r,x in P if a[r][x]==ic];r0,c0,l=min(r for r,_ in S),min(x for _,x in S),max(r for r,_ in S)-min(r for r,_ in S)+1
    for r in R(r0-l-1,r0+2*l+1):
     for x in R(c0-l-1,c0+2*l+1):
      if(r<r0-1 or r>r0+l)and(x<c0-1 or x>c0+l):continue
      o[r][x]=oc
    for r in R(r0-1,r0+l+1):
     for x in R(c0-1,c0+l+1):o[r][x]=ic
    for r in R(r0,r0+l):
     for x in R(c0,c0+l):o[r][x]=oc
 return o