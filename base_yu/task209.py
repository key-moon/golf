# best: 289(jailctf merger) / others: 290(jonas ryno kg583), 292(xsot ovs att joking mewheni), 312(4atj sisyphus luke Seek mukundan), 383(Afordancja), 393(kdmitrie)
def p(g):
 (u,l),*_,(d,r)=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==4]
 G=[g[i][l:r+1]for i in range(u,d+1)]
 for i in range(u,d+1):
  g[i][l:r+1]=[0]*(r+1-l)
#  A=[(i,j)for i in range(len(G))for j in range(len(G[0]))if G[i][j]|4!=4]
 for s in range(2,6):
  for y in range(6,68):
   for x in range(-6,68):
    if all(len(g)>(i+y)//s>-1<(j+x)//s<len(g[0])and g[(i+y)//s][(j+x)//s]==G[i][j]for i in range(len(G))for j in range(len(G[0]))if G[i][j]|4!=4):
    # if all(len(g)>(i+y)//s>-1<(j+x)//s<len(g[0])and g[(i+y)//s][(j+x)//s]==G[i][j] for i,j in A):
     for i in range(len(G)):
      for j in range(len(G[0])):
       if G[i][j]<1 and len(g)>(i+y)//s>-1<(j+x)//s<len(g[0]):
        G[i][j]=g[(i+y)//s][(j+x)//s]
     return G

# def p(g):
#  h,w=len(g),len(g[0])
#  I=[i for i,v in enumerate(sum(g,[])) if v==4]
#  l,r,u,d=I[0]%w,I[3]%w+1,I[0]//w,I[3]//w+1
#  G=[]
#  for i in range(u,d):
#   G+=[g[i][l:r]]
#   g[i][l:r]=[0]*(r-l)
#  H,W=len(G),len(G[0])
#  A=[(i,j)for i in range(H)for j in range(W)if G[i][j]|4!=4]
#  for s in range(2,5):
#   for y in range(-99,99):
#    for x in range(-99,99):
#     if all(h>(i+y)//s>-1<(j+x)//s<w and g[(i+y)//s][(j+x)//s]==G[i][j] for i,j in A):
#      for i in range(H):
#       for j in range(W):
#        if G[i][j]==0 and h>(i+y)//s>-1<(j+x)//s<w:
#         G[i][j]=g[(i+y)//s][(j+x)//s]
#      return G








