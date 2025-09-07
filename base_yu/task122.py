# best: 82(4atj sisyphus luke Seek mukundan) / others: 88(jailctf merger), 91(jacekwl Potatoman nauti), 94(xsot ovs att joking mewheni), 100(4atj sisyphus luke Seek), 101(nauti)
# ====================================== 82 ======================================
# p=lambda g:(g[0]+g[1]).count(3)==1and g[-2:][::[1,-1][len(g)%2]]+g[:-2]or[*zip(*p([*zip(*g)]))]
p=lambda g:(g[0]+g[3]).count(3)==1and g[-2:][::1|len(g)%-2]+g[:-2]or[*zip(*p([*zip(*g)]))]
