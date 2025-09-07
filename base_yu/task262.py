# best: 39(mukundan, 4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 42(kg583), 42(jonas ryno kg583), 42(duckyluuk), 42(HETHAT), 42(dbdr)
# ================= 39 ================
# p=lambda g:[[b"\2\4\3"[s.index(5)]]*3for s in g]
# p=lambda g:[[-s.index(5)%3+2]*3for s in g]
# p=lambda g:[[hash((*s,))%5+2]*3for s in g]
p=lambda g:[[3+s[1]%2-s[0]%2]*3for s in g]
# p=lambda g:[[hash((*s,1))%1+1]*3for s in g]

# 012
# 243
