# best: 82(luke, att) / others: 83(biz), 83(sisyphus), 84(Seek64), 85(mukundan), 85(joking+MWI)
# ====================================== 82 ======================================
# p=lambda g:[[max(max(s[j%10::10])for s in g[i%10::10])for j in range(len(g[i]))]for i in range(len(g))]
# p=lambda g:[[max((s+[0]+t)[j%10::10])for j in range(len(s))]for s,t in zip(g,(g+g[9:10]+g)[10:])]
p=lambda g:[[max((s+[0]+t)[j%10::10])for j in range(len(s))]for s,t in zip(g,g[10:]+[[0]]+g)]