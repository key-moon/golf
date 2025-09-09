# best: 75(jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 84(4atj sisyphus luke Seek mukundan), 84(4atj sisyphus luke Seek), 87(jacekwl Potatoman), 87(jacekw), 87(jacekwl)
# =================================== 75 ==================================
p=lambda g,R=range(21):[[g[0][k:=max(i!=j,abs(j-i)//(min(i,j)+2)*2)]|g[k][0]for j in R]for i in R]


# def p(g):
#  for i in range(21):
#   for j in range(21):
#    k=i!=j and max(1,abs(j-i)//(min(i,j)+2)*2)
#    g[i][j]=g[i][j]or g[0][k]|g[k][0]
#  return g

# def p(g):
#  for i in range(21):
#   for j in range(21):
#    if not g[i][j]:
#     if i==j:
#      g[i][j]=g[0][0]
#     elif max(i,j)<(min(i,j)+1)*2:
#      g[i][j]=g[1][0]|g[0][1]
#     else:
#      g[i][j]=g[j][i]
#  return g
