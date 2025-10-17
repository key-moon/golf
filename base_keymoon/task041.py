# best: 49(kabutack, jonas ryno kg583, JRKKX, THUNDER THUNDER, jailctf merger, JRK, natte, dbdr, 2F, cubbus, JRKXK, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, HETHAT, JRKX, ox jam, MasukenSamba, jonas ryno kg583 kabutack, intgrah jimboko awu macaque sammyuri, biz, import itertools) / others: 50(Tony Li), 50(Yuchen20), 50(adakoda), 50(Ravi Annaswamy), 63(sekken)
# lambda g,a=0:[[(a:=a^c)|c for c in r]for r in g]
# ====================== 49 =====================
p=lambda g,a=0:[[c|(a:=a^c)for c in r]for r in g]
