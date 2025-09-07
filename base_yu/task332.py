# best: 58(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 61(xsot ovs att joking mewheni), 64(nauti), 64(jacekwl Potatoman nauti), 64(mukundan), 66(intgrah jimboko awu macaque sammyuri)
# ========================== 58 ==========================
# p=lambda g:[[v*i/5for v,i in zip(s[::-1],[3,5]*10)][::-1]for s in g]
# p=lambda g:[[v*i for v,i in zip(s[::-1],[.6,1]*10)][::-1]for s in g]
# p=lambda g:[[v*[1,.6][(len(s)-i)%2]for i,v in enumerate(s)]for s in g]
# p=lambda g:[[v*i for v,i in zip(s,([1,.6]*99)[len(s):])]for s in g]
# p=lambda g:[[s[i]*.6**(len(s)-i&1)for i in range(len(s))]for s in g]
p=lambda g:[[v*.6**(len(s)-i&1)for i,v in enumerate(s)]for s in g]
