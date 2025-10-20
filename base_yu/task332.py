# best: 58(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 61(ox jam), 61(biz), 64(jacekwl Potatoman nauti), 64(jacekw Potatoman nauti natte), 64(jacekw Potatoman nauti)
# ========================== 58 ==========================
# p=lambda g:[[v*i/5for v,i in zip(s[::-1],[3,5]*10)][::-1]for s in g]
# p=lambda g:[[v*i for v,i in zip(s[::-1],[.6,1]*10)][::-1]for s in g]
# p=lambda g:[[v*[1,.6][(len(s)-i)%2]for i,v in enumerate(s)]for s in g]
# p=lambda g:[[v*i for v,i in zip(s,([1,.6]*99)[len(s):])]for s in g]
# p=lambda g:[[s[i]*.6**(len(s)-i&1)for i in range(len(s))]for s in g]
p=lambda g:[[v*.6**(len(s)-i&1)for i,v in enumerate(s)]for s in g]
