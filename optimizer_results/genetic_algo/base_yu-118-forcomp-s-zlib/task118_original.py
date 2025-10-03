C=len
B=range
A=abs
def p(g):
 D={(i,j)for i in B(C(g))for j in B(C(g[0]))if g[i][j]&2};E=3
 while 1:
  c,s,i,j=max((sum((i+~-A(k-1)*l,j+~-A(k-2)*l)in D for k in B(4)for l in B(k>0,s)),-s,i,j)for s in B(E,5)for i in B(C(g))for j in B(C(g[0])));E=-s
  if c<1:return g
  for k in B(4):
   for l in B(k>0,-s):
    if(i+~-A(k-1)*l,j+~-A(k-2)*l)in D:D-={(i+~-A(k-1)*l,j+~-A(k-2)*l)}
    elif C(g)>i+~-A(k-1)*l>-1<j+~-A(k-2)*l<C(g[0]):g[i+~-A(k-1)*l][j+~-A(k-2)*l]=8