# best: 57(jailctf merger, natte, 2F, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, ox jam, biz, import itertools) / others: 58(Yuchen20), 61(intgrah jimboko awu macaque sammyuri), 62(kambarakun), 62(cg-klogw), 62(cg-klogw-sekken)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
