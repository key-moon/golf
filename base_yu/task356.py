# best: 105(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, HIMAGINE THE FUTURE., ox jam, biz, intgrah jimboko awu macaque sammyuri) / others: 108(Tony Li), 108(Tony Li & Darren Amadeus Martin), 110(import itertools), 113(jacekwl Potatoman nauti), 113(jacekw Potatoman nauti natte)
# ================================================= 105 =================================================
# p=lambda g,E=enumerate:[[8*(8in{*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[max({*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
