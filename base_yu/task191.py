# best: 251(jailctf merger) / others: 255(xsot ovs att joking mewheni), 269(4atj sisyphus luke Seek mukundan), 326(MasukenSamba), 350(jonas ryno kg583), 352(intgrah jimboko awu macaque sammyuri)
def p(g):
 u=[s[s.index(1):23-s[::-1].index(1)]for s in g if 1 in s]
 for d in range(8):
  for i in range(-1,25-len(u)):
   for j in range(-1,25-len(u[0])):
    if all(u[k][l]&4==g[i+k][j+l]for k in range(len(u))for l in range(len(u[0]))if-1<i+k<23>j+l>-1):
     for k in range(len(u)):
      for l in range(len(u[0])):
       if-1<i+k<23>j+l>-1:
        g[i+k][j+l]=u[k][l]
  *g,=map(list,zip(*g))
  if d%4<3:g=g[::-1]
 return g


# def p(g):
#  u=[s[s.index(1):23-s[::-1].index(1)] for s in g if 1 in s]
#  for _ in range(8):
#   for i in range(-1,25-len(u)):
#    for j in range(-1,25-len(u[0])):
#     if all((u[k][l],g[i+k][j+l])in((1,0),(4,4))for k in range(len(u))for l in range(len(u[0]))if 0<=i+k<23 and 0<=j+l<23):
#      for k in range(len(u)):
#       for l in range(len(u[0])):
#        if 0<=i+k<23 and 0<=j+l<23:
#         g[i+k][j+l]=u[k][l]
#   *g,=map(list,zip(*g[::-1]))
#   if _%4==3:
#    g=g[::-1]
#  return g



