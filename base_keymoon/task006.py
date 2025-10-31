# best: 49(Code Golf International, lv1.dev, jailctf merger, HIMAGINE THE FUTURE.) / others: 51(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 51(4atj sisyphus luke Seek mukundan), 51(LogicLynx), 51(ALE-Agent), 51(santa2024)
#  b"012"
# (0,1,2)
# sum(r[i::4])
# r[i]+r[i+4]
# ====================== 49 =====================
p=lambda g:[[2*all(r[i::4])for i in(0,1,2)]for r in g]
