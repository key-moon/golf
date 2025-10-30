# best: 131(jailctf merger) / others: 136(ox jam), 137(HIMAGINE THE FUTURE.), 144(biz), 147(Code Golf International), 147(4atj sisyphus luke Seek mukundan)
# ============================================================== 131 ==============================================================
# p=lambda g,R=range:[[(g[i][j]==5)*5 or sum((g[i//4+k%3*4][j//4+k//3*4]==4)*g[i%4+k%3*4][j%4+k//3*4]for k in R(9))for j in R(11)]for i in R(11)]
# p=lambda g,R=range(11):[[(g[i][j]==5)*5 or sum((g[i//4+k%3*4][j//4+k//3*4]==4)*g[i%4+k%3*4][j%4+k//3*4]for k in R)for j in R]for i in R]
p=lambda g,R=range(11):[[(g[i][j]==5)*5or sum((g[i//4+k][j//4+l]==4)*g[i%4+k][j%4+l]for k in(0,4,8)for l in(0,4,8))for j in R]for i in R]
