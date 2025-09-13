# best: 255(4atj sisyphus luke Seek mukundan) / others: 261(natte), 281(xsot ovs att joking mewheni), 285(jailctf merger), 335(intgrah jimboko awu macaque sammyuri), 358(MasukenSamba)
# R=range
# def p(g):
#  for c in R(10):
#   S=[i for i,v in enumerate(sum(g,[]))if v==c]
#   if len(S)==0:
#    continue
#   L=[v%10 for v in S]
#   U=[v//10 for v in S]
#   w=max(L)-min(L)
#   h=max(U)-min(U)
#   for l in range(9-w):
#    for u in range(9-h):
#     if len(S)*5+sum(sum(s[l:l+w+2])for s in g[u:u+h+2])==(h+2)*(w+2)*5:
#      print(CASE,c,l,u)
#      for k in S:
#       g[k//10][k%10]=0
#      for s in g[u:u+h+2]:
#       for i in range(l,l+w+2):
#        if s[i]==0:
#         s[i]=c
#  return g


# R=range
# def p(g):
#  for l in R(10):
#   for u in R(10):
#    r=l
#    d=u
#    while r<10 and g[u][r]==5:r+=1
#    while d<10 and g[d][l]==5:d+=1
#    for c in R(10):
#     S=[i for i,v in enumerate(sum(g,[]))if v==c]
#     T=[i*10+j for i in R(u,d)for j in R(l,r)if g[i][j]<1]
#     if(len(S)==len(T))*(len({y-x for x,y in zip(S,T)})<2):
#      for x,y in zip(S,T):
#       g[y//10][y%10]=c
#       g[x//10][x%10]=0
#  return g



def p(g):
 for l in range(10):
  for u in range(10):
   for r in range(l,10):
    if g[u][r]!=5:break
   for d in range(u,10):
    if g[d][l]!=5:break
   for c in range(10):
    S=[i*10+j for i in range(10)for j in range(10)if g[i][j]==c]
    T=[i*10+j for i in range(u,d)for j in range(l,r) if g[i][j]==0]
    if len(S)==len(T) and len({y-x for x,y in zip(S,T)})==1:
     for x,y in zip(S,T):
      g[y//10][y%10]=c
      g[x//10][x%10]=0
 return g
