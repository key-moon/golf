def p(a,u=range):
 f=[e[:]for e in a]
 s=set()
 for e in u(len(a)-2):
  for l in u(len(a[0])):
   if a[e][l]and(e,l)not in s:
    i=a[e][l]
    if all(a[e+d][l]==i for d in u(3)):
     n=l
     while n<len(a[0])and all(a[e+d][n]==i for d in u(3)):
      for d in u(3):s.add((e+d,n))
      n+=1
     for d in u(l,n):
      if(d-l)%2==1:f[e+1][d]=0
 return f