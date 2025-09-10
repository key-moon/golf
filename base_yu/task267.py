# best: 46(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 52(xsot ovs att joking mewheni), 54(intgrah jimboko awu macaque sammyuri), 56(jacekwl Potatoman nauti), 56(jonas ryno kg583), 57(natte)
# ==================== 46 ====================
# p=lambda g:[[v and g[6][0]for v in s]for s in g[:6]+g[:1]]
p=lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# p=lambda g:[[(v>0)*g[6][0]for v in s]for s in g[:6]+g[:1]]








