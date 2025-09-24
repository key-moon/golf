# best: 51(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 53(jonas ryno kg583 kabutack), 53(cubbus), 53(jacekwl Potatoman nauti), 53(JRK), 53(blob2822)
#  b"012"
# (0,1,2)
# sum(r[i::4])
# r[i]+r[i+4]
# ======================= 51 ======================
p=lambda g:[[2*all(r[i::4])for i in(0,1,2)]for r in g]
