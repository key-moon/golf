# best: 63(JRKKX, THUNDER THUNDER, jailctf merger, natte, JRKXK, 4atj sisyphus luke Seek mukundan, Yuchen20, jacekw Potatoman nauti natte, Code Golf International, JRKX, ox jam, jacekw Potatoman nauti, import itertools) / others: 64(MasukenSamba), 68(jacekwl), 68(intgrah jimboko awu macaque sammyuri), 68(jacekwl Potatoman nauti), 68(biz)
# ============================= 63 ============================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]
