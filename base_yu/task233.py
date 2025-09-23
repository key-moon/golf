# best: 297(ox jam, jailctf merger) / others: 336(natte), 355(jacekw Potatoman nauti), 355(jacekwl Potatoman nauti), 367(4atj sisyphus luke Seek mukundan), 370(Rafael Pooja)
def p(g):
 u=[[*s]for s in g]
 for _ in range(80):
  u=[[*s]for s in zip(*u[("2, "*7in str(u[-1]))-2::-1])]
 for _ in range(8):
  for i in range(len(g)-2):
   for j in range(len(g[0])-2):
    for y in range(len(u)-2):
     for x in range(len(u[0])-2):
      if all([2==g[i+k][j+m],2!=g[i+k][j+m]|2][u[y+k][x+m]>0]for k in range(3)for m in range(3))*(u+[[1]*80]*3)[y-1][x+1]*(u+[[1]*80]*3)[y+3][x+1]:
       for k in range(3):
        for m in range(3):
         u[y+k][x+m]=g[i+k][j+m]
         g[i+k][j+m]=0
  u=[[*s]for s in zip(*u[::-1])]
 return u

# def p(g):
#  for u in range(len(g)):
#   for l in range(len(g[0])):
#    r=[*g[u],0].index(0,l)
#    d=[*(g[k][l]for k in range(len(g))),0].index(0,u)
#    if g[u][l]==2 and r-l>5<d-u:
#     t=[s[l:r]for s in g[u:d]]
#     for _ in range(8):
#      for i in range(len(g)-2):
#       for j in range(len(g[0])-2):
#        for y in range(len(t)-2):
#         for x in range(len(t[0])-2):
#          if all(g[i+k][j+m]==2 if t[y+k][x+m]==0 else g[i+k][j+m]|2!=2 for k in range(3)for m in range(3))*(y<1 or 0<t[y-1][x+1])*(y+4>len(t) or 0<t[y+3][x+1]):
#           for k in range(3):
#            for m in range(3):
#             t[y+k][x+m]=g[i+k][j+m]
#             g[i+k][j+m]=0
#      *t,=map(list,zip(*t[::-1]))
#     return t
