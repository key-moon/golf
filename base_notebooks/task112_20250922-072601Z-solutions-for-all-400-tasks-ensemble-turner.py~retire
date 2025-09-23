e=enumerate
def p(j):
 A=c=0
 for i,r in e(j):
  for k,v in e(r):A+=i*(v==3);c+=k*(v==3)
 A>>=1;c>>=1
 for i,r in e(j):
  for k,v in e(r):
   if v==2:r[k]=j[A-i][k]=j[i][c-k]=j[A-i][c-k]=2
 return j