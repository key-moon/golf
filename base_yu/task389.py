# best: 57(4atj sisyphus luke Seek mukundan, natte, jailctf merger, ox jam, 2F, biz) / others: 58(Yuchen20), 61(intgrah jimboko awu macaque sammyuri), 62(jacekw Potatoman nauti), 62(cg-klogw), 63(jonas ryno kg583 kabutack)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
