# best: 73(jailctf merger) / others: 76(Code Golf International), 76(4atj sisyphus luke Seek mukundan), 76(ox jam), 79(jonas ryno kg583 kabutack), 79(jacekwl Potatoman nauti)
# ================================== 73 =================================
p=lambda g,R=range(17):[[g[i][j]or(g[i%6][j%6]>0)*g[0][5]for j in R]for i in R]
# p=lambda g:[[v or(w>0)*g[0][5]for v,w in zip(s,t[:6]*3)]for s,t in zip(g,g[:6]*3)]
