# best: 51(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, ShadowPrompt Labs, import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 53(jonas ryno kg583 kabutack), 53(cubbus), 53(jacekwl Potatoman nauti), 53(jacekw Potatoman nauti natte), 53(JRK)
#  b"012"
# (0,1,2)
# sum(r[i::4])
# r[i]+r[i+4]
# ======================= 51 ======================
p=lambda g:[[2*all(r[i::4])for i in(0,1,2)]for r in g]
