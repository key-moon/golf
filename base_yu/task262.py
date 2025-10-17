# best: 39(jailctf merger, natte, cubbus, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, ox jam, intgrah jimboko awu macaque sammyuri, import itertools) / others: 40(kambarakun), 40(adakoda), 41(ShadowPrompt Labs), 42(kabutack), 42(jonas ryno kg583)
# ================= 39 ================
# p=lambda g:[[b"\2\4\3"[s.index(5)]]*3for s in g]
# p=lambda g:[[-s.index(5)%3+2]*3for s in g]
# p=lambda g:[[hash((*s,))%5+2]*3for s in g]
p=lambda g:[[3+s[1]%2-s[0]%2]*3for s in g]
# p=lambda g:[[hash((*s,1))%1+1]*3for s in g]

# 012
# 243
