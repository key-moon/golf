A=range
def p(g):
 for i in A(n:=len(g)):
  for l in A(n):
   if(s:=g[i])[r:=l]>8:
    while s[r:]>[8]:r+=1
    for t in g[i:]:
     for j in A(l,r):t[j]|=1
    for k in A(i-(u:=r-l>>1),i+u+1):
     for j in A(l-u,r+u):
      if-1<k<n>j>-1and g[k][j]<9:g[k][j]=3
 return g