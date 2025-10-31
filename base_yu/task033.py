# best: 71(Code Golf International) / others: 73(jailctf merger), 73(ox jam), 76(4atj sisyphus luke Seek mukundan), 77(lv1.dev), 77(LogicLynx)
# ================================= 71 ================================
p=lambda g,R=range(17):[[g[i][j]or(g[i%6][j%6]>0)*g[0][5]for j in R]for i in R]
# p=lambda g:[[v or(w>0)*g[0][5]for v,w in zip(s,t[:6]*3)]for s,t in zip(g,g[:6]*3)]
