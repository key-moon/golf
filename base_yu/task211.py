# best: 48(ShadowPrompt Labs, jailctf merger, natte, cubbus, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri, adakoda, import itertools) / others: 49(kabutack), 49(Tony Li), 49(jonas ryno kg583), 49(JRKKX), 49(jacekwl)
# ===================== 48 =====================
# p=lambda g:[g[i][::-1]+g[i]for i in(2,1,0,0,1,2,2,1,0)]
# p=lambda g:[s[::-1]+s for s in g[::-1]+g+g[::-1]]
# p=lambda g:[s[::-1]+s for s in((g[::-1]+g)*2)[:9]]
p=lambda g:[s[::-1]+s for s in(g[::-1]+g)*2][:9]
# p=lambda g:(u:=g[::-1])and[s[::-1]+s for s in u+g+u]
