# best: 54(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 58(4atj sisyphus luke Seek mukundan), 58(intgrah jimboko awu macaque sammyuri), 58(Yuchen20), 60(2F), 60(biz)
# ======================== 54 ========================
# lambda g:[[any(a)*3for a in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:eval("[any(a)*3for a in zip(g.pop(0),g[4])],"*4)
