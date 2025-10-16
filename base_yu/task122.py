# best: 75(jailctf merger) / others: 78(intgrah jimboko awu macaque sammyuri), 82(natte), 82(4atj sisyphus luke Seek mukundan), 82(jacekw Potatoman nauti natte), 82(ox jam)
# =================================== 75 ==================================
# p=lambda g:(g[0]+g[1]).count(3)==1and g[-2:][::[1,-1][len(g)%2]]+g[:-2]or[*zip(*p([*zip(*g)]))]
p=lambda g:(g[0]+g[3]).count(3)==1and g[-2:][::1|len(g)%-2]+g[:-2]or[*zip(*p([*zip(*g)]))]
