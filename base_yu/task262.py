# best: 39(cubbus, jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, santa2024, natte, import itertools, jailctf merger, HIMAGINE THE FUTURE., ox jam, intgrah jimboko awu macaque sammyuri) / others: 40(ALE-Agent), 40(FuunAgent), 40(kambarakun), 40(adakoda), 40(biz)
# ================= 39 ================
# p=lambda g:[[b"\2\4\3"[s.index(5)]]*3for s in g]
# p=lambda g:[[-s.index(5)%3+2]*3for s in g]
# p=lambda g:[[hash((*s,))%5+2]*3for s in g]
p=lambda g:[[3+s[1]%2-s[0]%2]*3for s in g]
# p=lambda g:[[hash((*s,1))%1+1]*3for s in g]

# 012
# 243
