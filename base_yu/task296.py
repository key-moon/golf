# best: 60(intgrah jimboko awu macaque sammyuri) / others: 63(jacekw Potatoman nauti natte), 63(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 63(JRKX), 63(Code Golf International), 63(4atj sisyphus luke Seek mukundan)
# =========================== 60 ===========================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]
