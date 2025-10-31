# best: 86(Code Golf International, 4atj sisyphus luke Seek mukundan, ox jam) / others: 87(jailctf merger), 94(FuunAgent), 95(LogicLynx), 98(intgrah jimboko awu macaque sammyuri), 100(ALE-Agent)
# ======================================== 86 ========================================
# p=lambda g,c=-1:c*g or p([*zip(*[[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in g])],c+1)
# p=lambda g,c=-1:c*g or p([[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or p([[v or sum({*s[:i]}&{*s[i:]})for i,v in enumerate(s)]for s in zip(*g)],c+1)

# p=lambda g:[[s[i]or sum({*s[:i]}&{*s[i:]})for i in range(len(s))]for s in g]
