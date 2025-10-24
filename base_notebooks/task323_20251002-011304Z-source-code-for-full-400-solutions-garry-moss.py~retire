def p(e):
 n=13;u=[n[:]for n in e]
 t,o=next((t,o)for t in range(n)for o in range(n)if e[t][o])
 for f,e in(-1,1),(1,-1):
  l,r=t,o
  while 1:
   for a in[0]*2:
    l+=f
    if 0<=l<n:u[l][r]=5
    else:break
   else:
    for a in[0]*2:
     r+=e
     if 0<=r<n:u[l][r]=5
     else:break
    else:continue
   break
 return u