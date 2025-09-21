# best: 105(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 113(jacekw Potatoman nauti), 113(intgrah jimboko awu macaque sammyuri), 113(jacekwl Potatoman nauti), 119(JRKX), 119(jonas ryno kg583 kabutack)
# ================================================= 105 =================================================
# p=lambda g,E=enumerate:[[8*(8in{*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[max({*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
