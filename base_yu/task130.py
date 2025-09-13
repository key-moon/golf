# best: 65(duckyluuk, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, Yuchen20, jacekwl, jacekwl Potatoman nauti, xsot ovs att joking mewheni) / others: 66(HETHAT), 68(kabutack), 69(MasukenSamba), 72(jonas ryno kg583), 85(J&R)
# ============================== 65 =============================
# p=lambda g:[[sum({*s[i*3:i*3+3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[sum({*s[i*3:][:3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[*map(lambda f:sum({*f}-{5}),zip(*[iter(s)]*3))]for s in g[1::3]]
# p=lambda g:[[sum({*f}-{5})for f in zip(*[iter(s)]*3)]for s in g[1::3]]
p=lambda g:[[sum({*s[i:i+3]}-{5})for i in(0,3,6)]for s in g[::3]]
