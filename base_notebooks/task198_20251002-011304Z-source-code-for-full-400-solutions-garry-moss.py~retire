z=len
o=range
def p(r):
 c=max(sum(r,[]))
 for u in range(4):
  r=list(map(list,zip(*r[::-1])))
  n,n=z(r),z(r[0])
  for u in o(n):
   if r[u].count(c)>n/2:
    for s in o(n):
     if r[u][s]==0:r[u][s]=4
 for u in range(10):
  for u in o(n):
   for s in o(n):
    if r[u][s]==4:
     for d,e in[[0,1],[0,-1],[1,0],[-1,0]]:
      if 0<=u+d<n and 0<=s+e<n and r[u+d][s+e]==0:r[u+d][s+e]=4
 r=[[3if s==0else s for s in u]for u in r]
 return r