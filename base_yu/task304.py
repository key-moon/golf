# best: 92(4atj sisyphus luke Seek mukundan, 2F, biz, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 93(kabutack), 101(duckyluuk), 101(cg), 104(MasukenSamba), 104(Yuchen20)
# =========================================== 92 ===========================================
# p=lambda g:[[g[i//3][j//3]==max(u:=sum(g,[]),key=u.count)and g[i%3][j%3]for j in range(9)]for i in range(9)]
p=lambda g:[[y*(x==max(u:=sum(g,g),key=u.count))for x in s for y in t]for s in g for t in g]

# p=lambda g,R=range(9):[[(g[i//3][j//3]==max(u:=sum(g,[]),key=u.count))*g[i%3][j%3]for j in R]for i in R]










