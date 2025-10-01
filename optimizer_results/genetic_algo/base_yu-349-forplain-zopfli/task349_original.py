B=len
A=range
def p(g):
 for i in A(B(g)):
  for l in A(B(g)):
   r=l
   while g[i][r:]>[8]:r+=1
   for t in g[i:]:
    for j in A(l,r):t[j]|=1
   for k in A(i-(r-l>>1),i+(r-l>>1)+1):
    for j in A(l-(r-l>>1),r+(r-l>>1)):
     if k in A(B(g))and j in A(B(g))and g[k][j]<9:g[k][j]=3
 return g