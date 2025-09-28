# best: 105(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 113(jacekwl Potatoman nauti), 113(jacekw Potatoman nauti natte), 113(jacekw Potatoman nauti), 113(intgrah jimboko awu macaque sammyuri), 119(jonas ryno kg583 kabutack)
# ================================================= 105 =================================================
# p=lambda g,E=enumerate:[[8*(8in{*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[max({*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
