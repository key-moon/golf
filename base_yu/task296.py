# best: 55(Code Golf International) / others: 60(jailctf merger), 60(intgrah jimboko awu macaque sammyuri), 62(ALE-Agent), 62(FuunAgent), 62(ox jam)
# ========================= 55 ========================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]
