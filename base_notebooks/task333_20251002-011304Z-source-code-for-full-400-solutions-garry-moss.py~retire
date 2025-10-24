a=len
r=range
def p(x):
 for z in range(4):
  x=list(map(list,zip(*x[::-1])))
  e,u=a(x),a(x[0])
  for z in r(e):
   if 3in x[z]:
    m=x[z].index(3)
    n=max(x[z][:m])
    if n>0:
     for u in r(x[z].index(n),m):x[z][u]=n
 return x