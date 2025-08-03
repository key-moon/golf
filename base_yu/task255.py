def p(g,case):
 n=len(g)
 c=max(sum(g,[]))
 for _ in[0]*4:
  for _ in[0]*2:
   u=[[*g[i],0,0,c].index(c)for i in range(n)]+[n]
   br=bl=bv=bw=-99
   for r in range(n+2):
    for l in range(r-2):
     if any((g+[[0]])[k][0]==3 for k in range(l,r)):
      continue
     w=min(u[l:r])
     d=sum(g[k][:w-1].count(0) for k in range(l+1,r-1))
    #  if d>10:
    #   print(l,r,d)
     if bv<d and w>3:
      bl,br,bv,bw=l,r,d,w
#    print(bl,br,bv,bw)
   if bv>5:
    if br-bl==3:
     bw-=1
    for k in range(bl+1,br-1):
     g[k][:bw-1]=[3]*(bw-1)
   else:
    break
  *g,=map(list,zip(*g[::-1]))
 return g