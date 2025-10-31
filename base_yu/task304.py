# best: 92(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, natte, import itertools, jailctf merger, HIMAGINE THE FUTURE., ox jam, 2F, biz, intgrah jimboko awu macaque sammyuri) / others: 93(JRKX), 93(ALE-Agent), 93(cg-klogw-sekken), 93(FuunAgent), 93(Ravi Annaswamy)
# =========================================== 92 ===========================================
# p=lambda g:[[g[i//3][j//3]==max(u:=sum(g,[]),key=u.count)and g[i%3][j%3]for j in range(9)]for i in range(9)]
p=lambda g:[[y*(x==max(u:=sum(g,g),key=u.count))for x in s for y in t]for s in g for t in g]

# p=lambda g,R=range(9):[[(g[i//3][j//3]==max(u:=sum(g,[]),key=u.count))*g[i%3][j%3]for j in R]for i in R]
