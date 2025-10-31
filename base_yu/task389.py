# best: 57(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, ALE-Agent, natte, import itertools, jailctf merger, ox jam, 2F, biz) / others: 58(FuunAgent), 58(Yuchen20), 61(HIMAGINE THE FUTURE.), 61(intgrah jimboko awu macaque sammyuri), 62(jacekw Potatoman nauti)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
