# best: 87(4atj sisyphus luke Seek, 4atj) / others: 93(luke/sisyphus/Seek), 93(sisyphus), 97(luke), 101(mukundan), 101(joking+MWI)
# ========================================= 87 ========================================
# p=lambda g,c=-1:c*g or p([*zip(*[[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in g])],c+1)
# p=lambda g,c=-1:c*g or p([[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or p([[v or sum({*s[:i]}&{*s[i:]})for i,v in enumerate(s)]for s in zip(*g)],c+1)

# p=lambda g:[[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in g]