# 類題: 031
# best: 51(xsot ovs att joking mewheni, jailctf merger) / others: 53(4atj sisyphus luke Seek mukundan), 53(4atj sisyphus luke Seek), 53(intgrah jimboko awu macaque sammyuri), 55(kg583), 55(cg)
# ======================= 51 ======================

#p=lambda g:[x[::-1]for r in g if(x:=[i for i in r if i])]
#p=lambda g:[[*filter(int,r[::-1])]for r in g if max(r)]
p=lambda g:[x[::-1]for r in g if(x:=[*filter(int,r)])]
