# best: 70(4atj sisyphus luke Seek mukundan) / others: 73(jailctf merger), 76(natte), 76(intgrah jimboko awu macaque sammyuri), 76(xsot ovs att joking mewheni), 94(kabutack)
# ================================ 70 ================================
# 34567890123456789012345678901234567890123456789012345678901234567890
# p=lambda g:[[v for v,t in zip(s,zip(*g))if len({*t})>2]for s in g if len({*s})>2]
# lambda g:[[v for*t,v in zip(*g,s)if len({*t})>2]for s in g if len({*s})>2]
# lambda g:[[t[0]for t in zip(s,*g)if len({*t})>2]for s in g if len({*s})>2]
p=lambda g:[R for s in g if(R:=[t[0]for t in zip(s,*g)if len({*t}&{*s})>2])]



