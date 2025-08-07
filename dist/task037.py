A=enumerate
def p(g):
 d={}
 for(i,r)in A(g):
  for(j,v)in A(r):
   if v:d.setdefault(v,[]).append((i,j))
 for(v,l)in d.items():
  i,j=l[0];x,y=l[1];B=(x>i)-(x<i);C=(y>j)-(y<j)
  while 1:
   g[i][j]=v
   if i==x and j==y:break
   i+=B;j+=C
 return g