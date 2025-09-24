# best: 48(cubbus, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 49(jonas ryno kg583 kabutack), 49(jacekwl Potatoman nauti), 49(JRK), 49(JRKX), 49(jacekwl)
# ===================== 48 =====================
# p=lambda g:[g[i][::-1]+g[i]for i in(2,1,0,0,1,2,2,1,0)]
# p=lambda g:[s[::-1]+s for s in g[::-1]+g+g[::-1]]
# p=lambda g:[s[::-1]+s for s in((g[::-1]+g)*2)[:9]]
p=lambda g:[s[::-1]+s for s in(g[::-1]+g)*2][:9]
# p=lambda g:(u:=g[::-1])and[s[::-1]+s for s in u+g+u]
