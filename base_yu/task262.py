# best: 39(cubbus, jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, natte, import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 40(kambarakun), 40(adakoda), 42(jonas ryno kg583 kabutack), 42(JRK), 42(JRKX)
# ================= 39 ================
# p=lambda g:[[b"\2\4\3"[s.index(5)]]*3for s in g]
# p=lambda g:[[-s.index(5)%3+2]*3for s in g]
# p=lambda g:[[hash((*s,))%5+2]*3for s in g]
p=lambda g:[[3+s[1]%2-s[0]%2]*3for s in g]
# p=lambda g:[[hash((*s,1))%1+1]*3for s in g]

# 012
# 243
