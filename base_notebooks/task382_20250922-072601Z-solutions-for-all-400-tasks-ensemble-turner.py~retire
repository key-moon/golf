n=range
q=len
def p(f,e=1):
 for i in n(4):
  f=list(map(list,zip(*f[::-1])))
  h,w=q(f),q(f[0])
  if e:
   for i in n(h):
    if f[i][0]==8 and f[0].count(2)+f[-1].count(2)>0:
     e=0
     for c in n(w):
      if f[0][c]==2:e+=1
      if f[-1][c]==2:e-=1
      if 0<=i+e<h:f[i+e][c]=8
     e=0
 return f