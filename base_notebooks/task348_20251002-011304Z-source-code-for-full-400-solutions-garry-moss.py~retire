def p(n,l=range):
 p,x,e,f=len(n),len(n[0]),0,0
 for i in l(p):
  for r in l(x):
   if n[i][r]:e,f=i+2,r
 def p(i,r,a):
  if 0<=r<x:n[i][r]=a
 for g in l(x):
  e,a=e-1,7+g%2
  for i in l(e):p(i,f-g,a);p(i,f+g,a)
 return n