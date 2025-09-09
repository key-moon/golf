# best: 54(jailctf merger) / others: 58(4atj sisyphus luke Seek mukundan), 60(biz), 60(HETHAT), 60(xsot ovs att joking mewheni), 61(intgrah jimboko awu macaque sammyuri)
# ======================== 54 ========================
# lambda g:[[any(a)*3for a in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:eval("[any(a)*3for a in zip(g.pop(0),g[4])],"*4)

