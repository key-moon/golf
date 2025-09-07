# best: 65(mukundan, 4atj sisyphus luke Seek mukundan, jacekwl Potatoman, xsot ovs att joking mewheni, duckyluuk, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri, jacekwl) / others: 66(HETHAT), 66(nauti), 68(kabutack), 69(MasukenSamba), 85(jonas ryno kg583)
# ============================== 65 =============================
# p=lambda g:[[sum({*s[i*3:i*3+3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[sum({*s[i*3:][:3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[*map(lambda f:sum({*f}-{5}),zip(*[iter(s)]*3))]for s in g[1::3]]
# p=lambda g:[[sum({*f}-{5})for f in zip(*[iter(s)]*3)]for s in g[1::3]]
p=lambda g:[[sum({*s[i:i+3]}-{5})for i in(0,3,6)]for s in g[::3]]
