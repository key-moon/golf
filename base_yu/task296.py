# best: 63(jacekw Potatoman nauti natte, JRKX, Code Golf International, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti, natte, JRKXK, import itertools, jailctf merger, Tony Li & Darren Amadeus Martin, Yuchen20, ox jam, THUNDER THUNDER, JRKKX) / others: 64(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 64(MasukenSamba), 68(jacekwl Potatoman nauti), 68(jacekwl), 68(biz)
# ============================= 63 ============================
# p=lambda g:[[*map(max,zip(s,s[-3:],t,t[-3:]))]for s,t in zip(g,g[-3:])]
# p=lambda g:[[*map(max,s,s[-3:],t,t[-3:])]for s,t in zip(g,g[-3:])]
p=lambda g:[[*map(max,s,s[4:],t,t[4:])]for s,t in zip(g,g[2:])]
