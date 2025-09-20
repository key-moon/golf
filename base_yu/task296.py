# best: 63(ox jam, 4atj sisyphus luke Seek mukundan, JRKX, jailctf merger, Yuchen20, xsot ovs att joking mewheni) / others: 64(MasukenSamba), 68(intgrah jimboko awu macaque sammyuri), 68(jacekwl), 68(jacekwl Potatoman nauti), 71(Bulmenisaurus)
# ============================= 63 ============================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]
