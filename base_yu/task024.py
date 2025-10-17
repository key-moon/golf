# best: 62(jailctf merger, natte, 2F, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, ox jam, intgrah jimboko awu macaque sammyuri, biz, import itertools) / others: 63(Yuchen20), 65(THUNDER THUNDER), 66(MasukenSamba), 67(kabutack), 67(jonas ryno kg583)
# ============================ 62 ============================
# p=lambda g:[[(1 in s)+3*(3 in s)or(2 in t)*2for t in zip(*g)]for s in g]
p=lambda g:[[max({*s}-{2})or(2 in t)*2for t in zip(*g)]for s in g]
