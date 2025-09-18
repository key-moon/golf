# best: 216(ox jam, xsot ovs att joking mewheni) / others: 218(jailctf merger), 218(Yuchen20), 222(natte), 242(MasukenSamba), 243(jacekwl Potatoman nauti)
def p(g):
#  *o,=eval("[5]*9,"*9)
 o=[[5]*9 for _ in range(9)]
 for i in range(len(g)-2):
  for j in range(len(g[i])-2):
#    if all(all(g[i+k][j:j+3])for k in range(3)):
  #  x=1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5)
  #  y=1+(g[i+2][j+1]!=5)-(g[i][j+1]!=5)
   for u in range(3*(g[i][j]>0)):
    o[(1+(g[i+2][j+1]!=5)-(g[i][j+1]!=5))*3+u][(1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5))*3:(1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5))*3+3]=g[i+u][j:j+3]
    # o[(1+(g[i+2][j+1]!=5)-(g[i][j+1]!=5))*3+u][(1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5))*3:(1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5))*3+3]=g[i+u][j:j+3]
   for u in range(3*(g[i][j]>0)):
    g[i+u][j:j+3]=[0]*3
 return o

# def p(g):
# #  *o,=eval("[5]*9,"*9)
#  o=[[5]*9 for _ in range(9)]
#  for i in range(len(g)-2):
#   for j in range(len(g[i])-2):
# #    if all(all(g[i+k][j:j+3])for k in range(3)):
#    x=1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5)
#    y=1+(g[i+2][j+1]!=5)-(g[i][j+1]!=5)
#    for u in range(3*(g[i][j]>0)):
#     o[y*3+u][x*3:x*3+3]=g[i+u][j:j+3]
#     # o[(1+(g[i+2][j+1]!=5)-(g[i][j+1]!=5))*3+u][(1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5))*3:(1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5))*3+3]=g[i+u][j:j+3]
#     g[i+u][j:j+3]=[0]*3
#  return o

# def p(g):
#  h,w=len(g),len(g[0])
#  *o,=eval("[5]*9,"*9)
#  for i in range(h-2):
#   for j in range(w-2):
#    if all(g[i][j:j+3]+g[i+1][j:j+3]+g[i+2][j:j+3]):
#     x=1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5)
#     y=1+(g[i+2][j+1]!=5)-(g[i][j+1]!=5)
#     for u in range(3):
#      for v in range(3):
#       o[y*3+u][x*3+v]=g[i+u][j+v]
#  return o

# def p(g):
#  h,w=len(g),len(g[0])
#  *o,=eval("[5]*9,"*9)
#  for i in range(h-2):
#   for j in range(w-2):
#    if g[i][j]:
#     x=1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5)
#     y=1+(g[i+2][j+1]!=5)-(g[i][j+1]!=5)
#     for u in range(3):
#      for v in range(3):
#       o[y*3+u][x*3+v]=g[i+u][j+v]
#       g[i+u][j+v]=0
#  return o
