# best: 46(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 50(intgrah jimboko awu macaque sammyuri), 52(ox jam), 52(xsot ovs att joking mewheni), 54(cubbus), 56(JRKX)
# ==================== 46 ====================
# p=lambda g:[[v and g[6][0]for v in s]for s in g[:6]+g[:1]]
p=lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# p=lambda g:[[(v>0)*g[6][0]for v in s]for s in g[:6]+g[:1]]
