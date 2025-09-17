# best: 54(jailctf merger, xsot ovs att joking mewheni) / others: 58(4atj sisyphus luke Seek mukundan), 58(Yuchen20), 60(2F), 60(biz), 60(HETHAT)
# ======================== 54 ========================
# lambda g:[[any(a)*3for a in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:eval("[any(a)*3for a in zip(g.pop(0),g[4])],"*4)
