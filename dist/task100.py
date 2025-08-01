def p(g):
 d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:
    t=d.setdefault(v,[i,i,j,j])
    t[0]=min(t[0],i);t[1]=max(t[1],i)
    t[2]=min(t[2],j);t[3]=max(t[3],j)
 k=max(d,key=lambda v:(d[v][1]-d[v][0]+1)*(d[v][3]-d[v][2]+1))
 return[[k]*2]*2