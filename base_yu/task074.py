# best: 91(mukundan, 4atj sisyphus luke Seek, luke/sisyphus/Seek) / others: 99(luke), 106(joking+MWI), 106(joking/MWI), 106(joking), 106(joking MeWhenI)
# =========================================== 91 ==========================================
# p=lambda g:[[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in range(30)]for i in range(30)]
# p=lambda g,c=-3:c*g or p([[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in range(30)]for i in range(30)],c+1)
p=lambda g,c=-3,R=range(30):c*g or p([[min(g[i][j],g[j][i],[*g[j],9,9][31-i])for j in R]for i in R],c+1)

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