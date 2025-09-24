# best: 82(natte, ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 91(jacekw Potatoman nauti), 91(jacekwl Potatoman nauti), 104(JRKX), 104(jonas ryno kg583 kabutack), 104(jonas ryno kg583)
# ====================================== 82 ======================================
# p=lambda g:(g[0]+g[1]).count(3)==1and g[-2:][::[1,-1][len(g)%2]]+g[:-2]or[*zip(*p([*zip(*g)]))]
p=lambda g:(g[0]+g[3]).count(3)==1and g[-2:][::1|len(g)%-2]+g[:-2]or[*zip(*p([*zip(*g)]))]
