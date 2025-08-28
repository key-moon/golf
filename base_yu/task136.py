# best: 107(4atj sisyphus luke Seek, sisyphus) / others: 113(xsot ovs), 113(Seek64), 113(joking), 113(xsot), 113(joking MeWhenI)
# ================================================== 107 ==================================================
p=lambda g,R=range(1,9):exec("for i in R:\n for j in R:a=-~g[i][j]%3-1;g[i-a][j-a]|=g[i][j]&g[i+a][j+a]\n"*9)or g

# def p(g,R=range):
#  for _ in R(10):
#   for i in R(1,9):
#    for j in R(1,9):
#     a=-~g[i][j]%3-1
#     g[i-a][j-a]|=g[i][j]&g[i+a][j+a]
#  return g
