# best: 57(Yuchen20, biz) / others: 62(ox jam), 63(jailctf merger), 64(ShadowPrompt Labs), 64(kabutack), 64(jonas ryno kg583)
# ========================== 57 =========================
# lambda g,R=range(16):[[1+(i+j)%max(g[i])for j in R]for i in R]
p=lambda g,R=range(16):[R:=[1+j%max(g[0])for j in R]for i in R]
