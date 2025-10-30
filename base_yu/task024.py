# best: 62(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, natte, import itertools, jailctf merger, HIMAGINE THE FUTURE., ox jam, 2F, biz, intgrah jimboko awu macaque sammyuri) / others: 63(Yuchen20), 65(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 65(THUNDER THUNDER), 66(MasukenSamba), 67(jonas ryno kg583 kabutack)
# ============================ 62 ============================
# p=lambda g:[[(1 in s)+3*(3 in s)or(2 in t)*2for t in zip(*g)]for s in g]
p=lambda g:[[max({*s}-{2})or(2 in t)*2for t in zip(*g)]for s in g]
