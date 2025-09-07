# best: 63(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, xsot ovs att joking mewheni, mukundan) / others: 64(MasukenSamba), 68(jacekwl Potatoman), 68(jacekwl), 71(Bulmenisaurus), 73(natte)
# ============================= 63 ============================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]
