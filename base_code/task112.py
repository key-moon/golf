def p(g):
 d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:
    if v not in d:d[v]=[0,i,i,j,j]
    a=d[v];a[0]+=1;a[1]=min(a[1],i);a[2]=max(a[2],i)
    a[3]=min(a[3],j);a[4]=max(a[4],j)
 for b,a in d.items():
  if a[0]==(a[2]-a[1]+1)*(a[4]-a[3]+1):break
 for o in d:
  if o!=b:break
 i0,i1,j0,j1=a[1:]
 s=i0+i1;t=j0+j1
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==o:
    rr=s-i;cc=t-j
    r[j]=o;g[i][cc]=o;g[rr][j]=o;g[rr][cc]=o
 return g
