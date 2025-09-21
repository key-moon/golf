# best: 86(4atj sisyphus luke Seek mukundan) / others: 87(jailctf merger), 93(ox jam), 93(xsot ovs att joking mewheni), 102(jacekw Potatoman nauti), 102(jacekwl Potatoman nauti)
# ======================================== 86 ========================================
# p=lambda g,c=-1:c*g or p([*zip(*[[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in g])],c+1)
# p=lambda g,c=-1:c*g or p([[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or p([[v or sum({*s[:i]}&{*s[i:]})for i,v in enumerate(s)]for s in zip(*g)],c+1)

# p=lambda g:[[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in g]
