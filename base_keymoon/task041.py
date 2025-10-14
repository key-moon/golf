# best: 49(jonas ryno kg583 kabutack, cubbus, jacekw Potatoman nauti natte, JRK, JRKX, 4atj sisyphus luke Seek mukundan, dbdr, jonas ryno kg583, HETHAT, natte, kabutack, JRKXK, import itertools, MasukenSamba, jailctf merger, ox jam, THUNDER THUNDER, 2F, biz, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 50(Tony Li), 50(adakoda), 50(Yuchen20), 62(Ravi Annaswamy), 63(jacekw Potatoman nauti)
# lambda g,a=0:[[(a:=a^c)|c for c in r]for r in g]
# ====================== 49 =====================
p=lambda g,a=0:[[c|(a:=a^c)for c in r]for r in g]
