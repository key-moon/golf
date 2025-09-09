# best: 169(jailctf merger) / others: 175(4atj sisyphus luke Seek mukundan), 187(xsot ovs att joking mewheni), 235(Potatoman), 235(jacekwl Potatoman nauti), 263(MasukenSamba)
# ================================================================================= 169 =================================================================================
def p(g):
 for l in range(14):
  for u in range(14):
   if g[u][l+6]==g[u+6][l]==5:
    for i in range(16):
     for j in range(16):
      if all(0**g[u+y+1][l+x+1]==0**g[i+y][j+x]for y in range(5)for x in range(5)):
       for y in range(5):
        for x in range(5):
         g[i+y][j+x]=g[i+y][j+x]and g[u+y+1][l+x+1]
 return g

# def p(g):
#  for l in range(14):
#   for u in range(14):
#    t=[*zip(*g[u:u+7])][l:l+7]
#    if {*t[0],*t[-1],*[s[0]for s in t],*[s[-1]for s in t]}=={5}:
#     for i in range(16):
#      for j in range(16):
#       if all(bool(t[k+1][l+1])==bool(g[i+l][j+k]) for k in range(5)for l in range(5)):
#        for k in range(5):
#         for l in range(5):
#          g[i+l][j+k]=g[i+l][j+k]and t[k+1][l+1]
#     return g



