# best: 63(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 64(MasukenSamba), 68(jacekwl), 68(jacekwl Potatoman nauti), 71(Bulmenisaurus), 73(natte)
# ============================= 63 ============================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]

