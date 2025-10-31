# best: 53(ox jam) / others: 55(Code Golf International), 57(4atj sisyphus luke Seek mukundan), 57(jailctf merger), 59(jacekw Potatoman nauti natte), 59(lv1.dev)
# ======================== 53 =======================
# 345678901234567890123456789012345678901234567890123456

p=lambda g,E=enumerate:[[v and(v,4)[min(i,j)%2]for j,v in E(s)]for i,s in E(g)]

# k 1 -> 4
# k 0 -> k
# 0 0 -> 0
# 0 1 -> 0

# 1 1 -> 4
# 1 0 -> k
# 0 0 -> 0
# 0 1 -> 0

# def p(g):
#  R=range(1,len(g))
#  for i in R:
#   for j in R:
#    if g[i-1][j-1]|4>4:
#     g[i][j]=4
#  return g
