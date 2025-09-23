def p(f):
 n=13;i=[n[:]for n in f]
 j,W=next((j,W)for j in range(n)for W in range(n)if f[j][W])
 for l,o in(-1,1),(1,-1):
  a,C=j,W
  while 1:
   for e in[0]*2:
    a+=l
    if 0<=a<n:i[a][C]=5
    else:break
   else:
    for e in[0]*2:
     C+=o
     if 0<=C<n:i[a][C]=5
     else:break
    else:continue
   break
 return i