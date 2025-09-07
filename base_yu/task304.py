# best: 92(mukundan, 4atj sisyphus luke Seek mukundan, biz, xsot ovs att joking mewheni, 4atj sisyphus luke Seek, jailctf merger) / others: 93(kabutack), 93(intgrah jimboko awu macaque sammyuri), 101(cg), 101(duckyluuk), 104(jacekwl Potatoman)
# =========================================== 92 ===========================================
# p=lambda g:[[g[i//3][j//3]==max(u:=sum(g,[]),key=u.count)and g[i%3][j%3]for j in range(9)]for i in range(9)]
p=lambda g:[[y*(x==max(u:=sum(g,g),key=u.count))for x in s for y in t]for s in g for t in g]

# p=lambda g,R=range(9):[[(g[i//3][j//3]==max(u:=sum(g,[]),key=u.count))*g[i%3][j%3]for j in R]for i in R]
