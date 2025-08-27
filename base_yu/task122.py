# best: 94(joking+MWI, joking/MWI, joking MeWhenI) / others: 100(4atj sisyphus luke Seek), 100(luke/sisyphus/Seek), 100(Seek64), 101(nauti), 107(mukundan)
# ============================================ 94 ============================================
# p=lambda g:(g[0]+g[1]).count(3)==1and g[-2:][::[1,-1][len(g)%2]]+g[:-2]or[*zip(*p([*zip(*g)]))]
p=lambda g:(g[0]+g[1]).count(3)==1and g[-2:][::1|-(len(g)%2)]+g[:-2]or[*zip(*p([*zip(*g)]))]
