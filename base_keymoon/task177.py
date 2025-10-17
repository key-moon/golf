# 類題: 031
# best: 51(jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 53(4atj sisyphus luke Seek mukundan), 53(biz), 54(ShadowPrompt Labs), 54(import itertools), 55(jonas ryno kg583 kabutack)
# ======================= 51 ======================

#p=lambda g:[x[::-1]for r in g if(x:=[i for i in r if i])]
#p=lambda g:[[*filter(int,r[::-1])]for r in g if max(r)]
p=lambda g:[x[::-1]for r in g if(x:=[*filter(int,r)])]
