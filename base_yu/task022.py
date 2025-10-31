# best: 91(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 92(jailctf merger), 95(ox jam), 97(FuunAgent), 99(lv1.dev), 101(LogicLynx)
# =========================================== 91 ==========================================
# p=lambda g,R=range:[[max(g[y+i][x+j]for y in R(9)for x in R(9)if g[y+1][x+1]==5)for j in R(3)]for i in R(3)]
p=lambda g,R=range:[[max(g[k//9+i][k%9+j]for k in R(81)if g[k//9+1][k%9+1]==5)for j in R(3)]for i in R(3)]
