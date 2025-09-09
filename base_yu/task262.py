# best: 39(4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 42(natte), 42(duckyluuk), 42(MasukenSamba), 42(dbdr), 42(kabutack)
# ================= 39 ================
# p=lambda g:[[b"\2\4\3"[s.index(5)]]*3for s in g]
# p=lambda g:[[-s.index(5)%3+2]*3for s in g]
# p=lambda g:[[hash((*s,))%5+2]*3for s in g]
p=lambda g:[[3+s[1]%2-s[0]%2]*3for s in g]
# p=lambda g:[[hash((*s,1))%1+1]*3for s in g]

# 012
# 243


