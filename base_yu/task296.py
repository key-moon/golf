# best: 63(mukundan, 4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni, 4atj sisyphus luke Seek, jailctf merger) / others: 64(MasukenSamba), 68(jacekwl Potatoman), 68(jacekwl), 71(Bulmenisaurus), 73(HETHAT)
# ============================= 63 ============================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]
