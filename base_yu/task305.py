# best: 57(biz, Yuchen20) / others: 62(ox jam), 62(xsot ovs att joking mewheni), 63(jailctf merger), 64(4atj sisyphus luke Seek mukundan), 64(JRKX)
# ========================== 57 =========================
# lambda g,R=range(16):[[1+(i+j)%max(g[i])for j in R]for i in R]
p=lambda g,R=range(16):[R:=[1+j%max(g[0])for j in R]for i in R]
