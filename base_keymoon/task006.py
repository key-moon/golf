# best: 49(HIMAGINE THE FUTURE.) / others: 51(Code Golf International), 51(4atj sisyphus luke Seek mukundan), 51(ShadowPrompt Labs), 51(import itertools), 51(jailctf merger)
#  b"012"
# (0,1,2)
# sum(r[i::4])
# r[i]+r[i+4]
# ====================== 49 =====================
p=lambda g:[[2*all(r[i::4])for i in(0,1,2)]for r in g]
