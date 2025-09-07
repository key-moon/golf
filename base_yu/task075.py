# best: 86(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, mukundan) / others: 88(intgrah jimboko awu macaque sammyuri), 88(xsot ovs att joking mewheni), 95(MasukenSamba), 95(kg583), 95(jonas ryno kg583)
# ======================================== 86 ========================================
# p=lambda g:[g[i][:4]+[g[i//3*3+1][4+j//3*3+1]*g[i%3][j%3]for j in range(9)]for i in range(9)]
p=lambda g,R=range(9):[g[i][:4]+[g[i//3*3+1][4+j//3*3+1]*g[i%3][j%3]for j in R]for i in R]
