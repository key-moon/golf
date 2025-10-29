A=range
def p(g):
 c=max(g[0])
 for _ in A(4):
  g[::-1]=zip(*g);t=[30]+[[*s,c].index(c)for s in g]+[30];d=set()
  while 1:
   C,B,l,r=max((min(t[l:r])*(r-l-1),min(t[l:r])-1,l,r)for r in A(len(t)+1)for l in A(r-2)if not{l,r-1}&d)
   if C<25or B<5:break
   d|={*A(l,r)};B-=2*(r-l<5)
   for i in A(l,r-2):g[i]=(3,)*B+g[i][B:]
 return g