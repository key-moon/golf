# best: 57(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, natte, import itertools, jailctf merger, ox jam, 2F, biz) / others: 58(Yuchen20), 61(HIMAGINE THE FUTURE.), 61(intgrah jimboko awu macaque sammyuri), 62(jacekw Potatoman nauti), 62(cg-klogw-sekken)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
