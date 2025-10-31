# best: 212(ox jam) / others: 222(Code Golf International), 233(jailctf merger), 239(intgrah jimboko awu macaque sammyuri), 246(FuunAgent), 257(lv1.dev)
def p(g):
 c=max(g[0])
 for _ in range(4):
  g[::-1]=zip(*g)
  t=[30]+[[*s,c].index(c)for s in g]+[30]
  d=set()
  while 1:
   S,W,l,r=max((min(t[l:r])*(r-l-1),min(t[l:r])-1,l,r)for r in range(len(t)+1)for l in range(r-2)if not{l,r-1}&d)
   if S<25 or W<5:break
   d|={*range(l,r)}
   W-=2*(r-l<5)
   for i in range(l,r-2):
    g[i]=(3,)*W+g[i][W:]
 return g

# def p(g,case):
#  n=len(g)
#  c=max(sum(g,[]))
#  for _ in[0]*4:
#   for _ in[0]*2:
#    u=[[*g[i],0,0,c].index(c)for i in range(n)]+[n]
#    br=bl=bv=bw=-99
#    for r in range(n+2):
#     for l in range(r-2):
#      if any((g+[[0]])[k][0]==3 for k in range(l,r)):
#       continue
#      w=min(u[l:r])
#      d=sum(g[k][:w-1].count(0) for k in range(l+1,r-1))
#     #  if d>10:
#     #   print(l,r,d)
#      if bv<d and w>3:
#       bl,br,bv,bw=l,r,d,w
# #    print(bl,br,bv,bw)
#    if bv>5:
#     if br-bl==3:
#      bw-=1
#     for k in range(bl+1,br-1):
#      g[k][:bw-1]=[3]*(bw-1)
#    else:
#     break
#   *g,=map(list,zip(*g[::-1]))
#  return g
