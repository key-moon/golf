# best: 57(ox jam, 4atj sisyphus luke Seek mukundan, 2F, biz, jailctf merger) / others: 58(Yuchen20), 61(intgrah jimboko awu macaque sammyuri), 62(jacekw Potatoman nauti), 62(cg-klogw), 63(JRKX)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
