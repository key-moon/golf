# best: 86(luke, luke/sisyphus/Seek) / others: 88(Seek64), 95(kg583), 99(duckyluuk), 100(mukundan), 103(kabutack)
# ======================================== 86 ========================================
# p=lambda g:[g[i][:4]+[g[i//3*3+1][4+j//3*3+1]*g[i%3][j%3]for j in range(9)]for i in range(9)]
p=lambda g,R=range(9):[g[i][:4]+[g[i//3*3+1][4+j//3*3+1]*g[i%3][j%3]for j in R]for i in R]