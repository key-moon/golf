# best: 92(jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, natte, jailctf merger, ox jam, 2F, biz, intgrah jimboko awu macaque sammyuri) / others: 93(JRKX), 93(kabutack), 93(cg-klogw), 101(cg), 101(duckyluuk)
# =========================================== 92 ===========================================
# p=lambda g:[[g[i//3][j//3]==max(u:=sum(g,[]),key=u.count)and g[i%3][j%3]for j in range(9)]for i in range(9)]
p=lambda g:[[y*(x==max(u:=sum(g,g),key=u.count))for x in s for y in t]for s in g for t in g]

# p=lambda g,R=range(9):[[(g[i//3][j//3]==max(u:=sum(g,[]),key=u.count))*g[i%3][j%3]for j in R]for i in R]
