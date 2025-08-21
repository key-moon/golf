# best: 62(luke) / others: 63(4atj), 63(att), 65(mukundan), 69(Seek64), 70(biz)
# ============================ 62 ============================
# p=lambda g:[g[i][:4]+[g[2][i],g[1][i],g[0][i]]+g[2-i][3::-1]for i in(0,1,2)]
# p=lambda g:[s[:4]+[z,y,x]+t[3::-1]for s,(x,y,z),t in zip(g,[*zip(*g)][:3],g[::-1])]
p=lambda g:[s[:4]+[*t]+u[3::-1]for s,t,u in zip(g,zip(*g[::-1]),g[::-1])]
