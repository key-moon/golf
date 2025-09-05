# best: 105(mukundan, 4atj sisyphus luke Seek, sisyphus) / others: 108(Seek64), 129(joking), 129(joking MeWhenI), 137(natte), 137(MeWhenI)
# ================================================= 105 =================================================
# p=lambda g,E=enumerate:[[8*(8in{*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[max({*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]