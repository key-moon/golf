# best: 86(jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 88(ox jam), 95(jonas ryno kg583 kabutack), 95(JRKX), 95(jonas ryno kg583), 95(MasukenSamba)
# ======================================== 86 ========================================
# p=lambda g:[g[i][:4]+[g[i//3*3+1][4+j//3*3+1]*g[i%3][j%3]for j in range(9)]for i in range(9)]
#p=lambda g,R=range(9):[g[i][:4]+[g[i//3*3+1][4+j//3*3+1]*g[i%3][j%3]for j in R]for i in R]
p=lambda g,R=range(9):[g[i][:4]+[g[i//3*3+1][j//3*3+5]*g[i%3][j%3]for j in R]for i in R]
