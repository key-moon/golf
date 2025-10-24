def p(o):
 u=range;r=len(o);i=[[0]*r for o in u(r)];m,o=0,0;a=[(0,1),(1,0),(0,-1),(-1,0)]
 for l in u(r):
  i[m][o]=3
  if l<r-1:o+=1
 r=r-1;f=1
 while r>0:
  for l in u(2):
   if r>0:
    m,o=m+a[f][0],o+a[f][1]
    for l in u(r):
     i[m][o]=3
     if l<r-1:m,o=m+a[f][0],o+a[f][1]
    f=(f+1)%4
  r-=2
 return i