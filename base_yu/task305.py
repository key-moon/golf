# best: 56(biz) / others: 57(Code Golf International), 57(lv1.dev), 57(LogicLynx), 57(FuunAgent), 57(Yuchen20)
# ========================= 56 =========================
# lambda g,R=range(16):[[1+(i+j)%max(g[i])for j in R]for i in R]
p=lambda g,R=range(16):[R:=[1+j%max(g[0])for j in R]for i in R]
