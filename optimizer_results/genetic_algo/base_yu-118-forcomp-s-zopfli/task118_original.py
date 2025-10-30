C=len
B=abs
A=range
def p(g):
 D={(i,j)for i in A(C(g))for j in A(C(g[0]))if g[i][j]&2};E=3
 while 1:
  c,s,i,j=max((sum((i+~-B(k-1)*l,j+~-B(k-2)*l)in D for k in A(4)for l in A(k>0,s)),-s,i,j)for s in A(E,5)for i in A(C(g))for j in A(C(g[0])));E=-s
  if c<1:return g
  for k in A(4):
   for l in A(k>0,-s):
    if(i+~-B(k-1)*l,j+~-B(k-2)*l)in D:D-={(i+~-B(k-1)*l,j+~-B(k-2)*l)}
    elif i+~-B(k-1)*l in A(C(g))and j+~-B(k-2)*l in A(C(g[0])):g[i+~-B(k-1)*l][j+~-B(k-2)*l]=8