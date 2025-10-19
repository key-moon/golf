# best: 50(jailctf merger, 4atj sisyphus luke Seek mukundan, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri, import itertools) / others: 54(ShadowPrompt Labs), 54(Tony Li), 54(natte), 54(Yuchen20), 54(jacekw Potatoman nauti natte)
# ====================== 50 ======================
# p=lambda g:[[s[i]|s[i+3]and 6for i in range(3)]for s in g]
# p=lambda g:[[x|y and 6for x,y in zip(s,s[3:])]for s in g]
# p=lambda g:[[(x|y>0)*6for x,y in zip(s,s[3:])]for s in g]
p=lambda g:[eval("6*(s.pop(0)+s[2]>0),"*3)for s in g]
