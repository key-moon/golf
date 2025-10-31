# best: 50(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, ALE-Agent, santa2024, import itertools, jailctf merger, ox jam, biz, intgrah jimboko awu macaque sammyuri) / others: 53(HIMAGINE THE FUTURE.), 54(jacekw Potatoman nauti natte), 54(Team JYCDT), 54(HETHAT), 54(FuunAgent)
# ====================== 50 ======================
# p=lambda g:[[s[i]|s[i+3]and 6for i in range(3)]for s in g]
# p=lambda g:[[x|y and 6for x,y in zip(s,s[3:])]for s in g]
# p=lambda g:[[(x|y>0)*6for x,y in zip(s,s[3:])]for s in g]
p=lambda g:[eval("6*(s.pop(0)+s[2]>0),"*3)for s in g]
