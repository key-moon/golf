# best: 55(natte, ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, HETHAT, xsot ovs att joking mewheni) / others: 56(dbdr), 56(Yuchen20), 59(jonas ryno kg583), 59(JRK), 64(MasukenSamba)
# 72
# p=lambda g:[[(t:=sum({*r,*s}))and[t,2][10<t]for s in zip(*g)]for r in g]
# 56
p=lambda g:[[sum({*r,*s})%13for s in zip(*g)]for r in g]
