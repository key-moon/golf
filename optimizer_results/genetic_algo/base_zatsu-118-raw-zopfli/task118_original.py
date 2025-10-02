C=len
B=range
A=abs
def p(l):
 v={(i,j)for i in B(C(l))for j in B(C(l[0]))if l[i][j]&2};y=3
 while 1:
  c,k,i,j=max((sum((i+~-A(q-1)*g,j+~-A(q-2)*g)in v for q in B(4)for g in B(q>0,k)),-k,i,j)for k in B(y,5)for i in B(C(l))for j in B(C(l[0])));y=-k
  if c<1:return l
  for q in B(4):
   for g in B(q>0,-k):
    if(i+~-A(q-1)*g,j+~-A(q-2)*g)in v:v-={(i+~-A(q-1)*g,j+~-A(q-2)*g)}
    elif C(l)>i+~-A(q-1)*g>-1<j+~-A(q-2)*g<C(l[0]):l[i+~-A(q-1)*g][j+~-A(q-2)*g]=8