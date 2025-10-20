# best: 77(jailctf merger) / others: 79(Code Golf International), 79(4atj sisyphus luke Seek mukundan), 80(ox jam), 83(intgrah jimboko awu macaque sammyuri), 84(MasukenSamba)
# ==================================== 77 ===================================
# lambda g:[[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in range(30)]for i in range(30)]
# lambda g,c=-3:c*g or p([[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in range(30)]for i in range(30)],c+1)
# lambda g,c=-3,R=range(30):c*g or p([[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in R]for i in R],c+1)

# lambda*G:[*{*G}-{9},-1][0]if G[0]*0==0else[*map(p,*sum([[g,g[:2]+g[::-1]]for g in G],[]))]
# lambda*G:[*{*G}-{9},-1][0]if G[0]*0==0else[*map(p,*sum([[g,g[:2]+g[::-1]]for g in G],[]))] <- failed

# lambda g,c=-9:c*g or[*zip(*[[[*{*s}-{9},9][0]for s in zip(r,r[:2]+r[::-1])]for r in p(g,c+1)])]
# lambda g,c=-9:c*g or p([[[*{*s}-{9},9][0]for s in zip(r,[9]*2+r[::-1],R)]for*R,r in zip(*g,g)],c+1)
# p=lambda g,c=-9:c*g or p([[[*{*s}-{9},9][0]for s in zip(r,[9]*2+r[::-1],R)]for*R,r in zip(*g,g)],c+1)
# p=lambda g,c=-9:c*g or p([[min(s)for s in zip(r,[9]*2+r[::-1],R)]for*R,r in zip(*g,g)],c+1)
p=lambda g,c=-9:c*g or p([[*map(min,r,[9]*2+r[::-1],R)]for*R,r in zip(*g,g)],c+1)


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
