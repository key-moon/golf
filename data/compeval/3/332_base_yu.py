# best: 58(luke) / others: 64(mukundan), 64(nauti), 65(4atj), 65(sisyphus), 67(kg583)
# ========================== 58 ==========================
# p=lambda g:[[v*i/5for v,i in zip(s[::-1],[3,5]*10)][::-1]for s in g]
# p=lambda g:[[v*i for v,i in zip(s[::-1],[.6,1]*10)][::-1]for s in g]
# p=lambda g:[[v*[1,.6][(len(s)-i)%2]for i,v in enumerate(s)]for s in g]
# p=lambda g:[[v*i for v,i in zip(s,([1,.6]*99)[len(s):])]for s in g]
# p=lambda g:[[s[i]*.6**(len(s)-i&1)for i in range(len(s))]for s in g]
p=lambda g:[[v*.6**(len(s)-i&1)for i,v in enumerate(s)]for s in g]
