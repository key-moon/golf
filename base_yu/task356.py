# best: 105(jailctf merger, 4atj sisyphus luke Seek mukundan, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri) / others: 108(Tony Li), 113(jacekw Potatoman nauti natte), 113(jacekwl Potatoman nauti), 113(jacekw Potatoman nauti), 113(import itertools)
# ================================================= 105 =================================================
# p=lambda g,E=enumerate:[[8*(8in{*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[max({*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
