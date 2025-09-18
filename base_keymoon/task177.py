# 類題: 031
# best: 51(ox jam, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 53(4atj sisyphus luke Seek mukundan), 55(natte), 55(MasukenSamba), 55(kabutack), 55(cg)
# ======================= 51 ======================

#p=lambda g:[x[::-1]for r in g if(x:=[i for i in r if i])]
#p=lambda g:[[*filter(int,r[::-1])]for r in g if max(r)]
p=lambda g:[x[::-1]for r in g if(x:=[*filter(int,r)])]
