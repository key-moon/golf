# best: 108(jailctf merger) / others: 115(xsot ovs att joking mewheni), 117(mukundan), 129(4atj sisyphus luke Seek), 141(dbdr), 143(Afordancja)
# ================================================== 108 ===================================================
# lambda g,E=enumerate:[[v*(1<str([(),*zip(*[[0]*99,*g][i:i+3])][j:j+3]).count(str(v)))for j,v in E(r)]for i,r in E(g)]
p=lambda g,E=enumerate:[[v*(v<sum(sum([(),*zip(*[[0]*99,*g][i:i+3])][j:j+3],())))for j,v in E(r)]for i,r in E(g)]
