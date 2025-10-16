# best: 51(ShadowPrompt Labs, jailctf merger, 4atj sisyphus luke Seek mukundan, ox jam, intgrah jimboko awu macaque sammyuri, import itertools) / others: 53(kabutack), 53(Tony Li), 53(jonas ryno kg583), 53(sekken), 53(JRKKX)
#  b"012"
# (0,1,2)
# sum(r[i::4])
# r[i]+r[i+4]
# ======================= 51 ======================
p=lambda g:[[2*all(r[i::4])for i in(0,1,2)]for r in g]
