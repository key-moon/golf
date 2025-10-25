# best: 107(intgrah jimboko awu macaque sammyuri) / others: 109(Code Golf International), 109(4atj sisyphus luke Seek mukundan), 109(jailctf merger), 109(ox jam), 109(2F)
# ================================================== 107 ==================================================
# p=lambda g,E=enumerate:[[s[j]or sum(({*s[:j]}&{*s[j:]})-{0,g[0][2]}) or sum(({*t[:i]}&{*t[i:]})-{0,g[0][2]}) for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or sum(({*s[:j:3]}&{*s[j::3]}|{*t[:i:3]}&{*t[i::3]}))for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[s[j]|sum({*s[:j:3]}&{*s[j::3]}|{*t[:i:3]}&{*t[i::3]})for j,t in E(zip(*g))]for i,s in E(g)]
