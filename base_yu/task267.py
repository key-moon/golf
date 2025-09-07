# best: 46(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 51(mukundan), 52(xsot ovs att joking mewheni), 54(intgrah jimboko awu macaque sammyuri), 56(kg583), 56(jonas ryno kg583)
# ==================== 46 ====================
# p=lambda g:[[v and g[6][0]for v in s]for s in g[:6]+g[:1]]
p=lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# p=lambda g:[[(v>0)*g[6][0]for v in s]for s in g[:6]+g[:1]]
