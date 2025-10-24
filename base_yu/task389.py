# best: 57(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, natte, import itertools, jailctf merger, ox jam, 2F, biz) / others: 58(Yuchen20), 61(intgrah jimboko awu macaque sammyuri), 62(jacekw Potatoman nauti), 62(cg-klogw-sekken), 62(kambarakun)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
