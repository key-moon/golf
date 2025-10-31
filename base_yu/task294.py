# best: 70(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, lv1.dev, FuunAgent, import itertools, jailctf merger, HIMAGINE THE FUTURE., ox jam, THUNDER THUNDER) / others: 76(jonas ryno kg583 kabutack), 76(JRK), 76(JRKX), 76(4atj sisyphus luke Seek mukundan), 76(Team JYCDT)
# ================================ 70 ================================
# p=lambda g:[[(0<i<9>j>0and g[i-1][j]==g[i][j-1]==g[i+1][j]==g[i][j+1]>0)*2 or g[i][j] for j in range(10)]for i in range(10)]
# p=lambda g,R=range(10):[[(0<i<9>j>0and g[i-1][j]==g[i][j-1]==g[i+1][j]==g[i][j+1]>0)*2or g[i][j]for j in R]for i in R]
p=lambda g,R=range(10):[[(0<i<9>j>0and{g[i-1][j],g[i+1][j],*g[i][j-1:j+2]}=={5})*2or g[i][j]for j in R]for i in R]
