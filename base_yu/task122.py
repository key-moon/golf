# best: 70(Code Golf International) / others: 71(ox jam), 75(jailctf merger), 78(import itertools), 78(intgrah jimboko awu macaque sammyuri), 80(LogicLynx)
# ================================ 70 ================================
# p=lambda g:(g[0]+g[1]).count(3)==1and g[-2:][::[1,-1][len(g)%2]]+g[:-2]or[*zip(*p([*zip(*g)]))]
p=lambda g:(g[0]+g[3]).count(3)==1and g[-2:][::1|len(g)%-2]+g[:-2]or[*zip(*p([*zip(*g)]))]
