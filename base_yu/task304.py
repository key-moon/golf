# best: 92(jailctf merger, natte, 2F, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri, biz, import itertools) / others: 93(ShadowPrompt Labs), 93(kabutack), 93(JRKKX), 93(THUNDER THUNDER), 93(JRKXK)
# =========================================== 92 ===========================================
# p=lambda g:[[g[i//3][j//3]==max(u:=sum(g,[]),key=u.count)and g[i%3][j%3]for j in range(9)]for i in range(9)]
p=lambda g:[[y*(x==max(u:=sum(g,g),key=u.count))for x in s for y in t]for s in g for t in g]

# p=lambda g,R=range(9):[[(g[i//3][j//3]==max(u:=sum(g,[]),key=u.count))*g[i%3][j%3]for j in R]for i in R]
