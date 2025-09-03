# best: 79(4atj sisyphus luke Seek) / others: 80(jailctf merger), 81(mukundan), 81(xsot ovs att joking mewheni), 107(natte), 110(duckyluuk)
# ===================================== 79 ====================================
# lambda g:[[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in range(30)]for i in range(30)]
# lambda g,c=-3:c*g or p([[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in range(30)]for i in range(30)],c+1)
# lambda g,c=-3,R=range(30):c*g or p([[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in R]for i in R],c+1)

# lambda*G:[*{*G}-{9},-1][0]if G[0]*0==0else[*map(p,*sum([[g,g[:2]+g[::-1]]for g in G],[]))]
# lambda*G:[*{*G}-{9},-1][0]if G[0]*0==0else[*map(p,*sum([[g,g[:2]+g[::-1]]for g in G],[]))] <- failed

p=lambda g,R=range(30):[[[*{g[i][j],g[j][i],[*g[i],9][-j],(g[:2]+g[::-1])[i][j]}-{9},-1][0]for j in R]for i in R]


# def p(g):
#  for I in range(30*30*4):
#   if g[j:=I%30][i:=I//30%30]<9:g[i][j]=g[j][i]
#   if j>1 and g[i][31-j]<9:g[i][j]=g[i][31-j]
#  return g

# def p(g):
#  for _ in range(2):
#   for i in range(30):
#    for j in range(30):
#     if i>1 and g[31-i][j]<9:
#      g[i][j]=g[31-i][j]
#     if g[j][i]<9:
#      g[i][j]=g[j][i]
#  return g
