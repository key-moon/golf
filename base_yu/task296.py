# best: 63(jacekw Potatoman nauti natte, JRKX, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti, natte, JRKXK, import itertools, jailctf merger, Yuchen20, ox jam, JRKKX) / others: 64(MasukenSamba), 68(jacekwl Potatoman nauti), 68(jacekwl), 68(intgrah jimboko awu macaque sammyuri), 71(Tony Li)
# ============================= 63 ============================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]
