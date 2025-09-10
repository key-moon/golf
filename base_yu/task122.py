# best: 82(4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni) / others: 88(jailctf merger), 91(jacekwl Potatoman nauti), 104(jonas ryno kg583), 108(JRK), 109(2F)
# ====================================== 82 ======================================
# p=lambda g:(g[0]+g[1]).count(3)==1and g[-2:][::[1,-1][len(g)%2]]+g[:-2]or[*zip(*p([*zip(*g)]))]
p=lambda g:(g[0]+g[3]).count(3)==1and g[-2:][::1|len(g)%-2]+g[:-2]or[*zip(*p([*zip(*g)]))]








