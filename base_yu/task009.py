# best: 95(Code Golf International) / others: 107(intgrah jimboko awu macaque sammyuri), 108(LogicLynx), 108(jailctf merger), 109(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 109(4atj sisyphus luke Seek mukundan)
# ============================================= 95 ============================================
# p=lambda g,E=enumerate:[[s[j]or sum(({*s[:j]}&{*s[j:]})-{0,g[0][2]}) or sum(({*t[:i]}&{*t[i:]})-{0,g[0][2]}) for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or sum(({*s[:j:3]}&{*s[j::3]}|{*t[:i:3]}&{*t[i::3]}))for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[s[j]|sum({*s[:j:3]}&{*s[j::3]}|{*t[:i:3]}&{*t[i::3]})for j,t in E(zip(*g))]for i,s in E(g)]
