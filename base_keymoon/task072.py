# best: 54(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 60(4atj sisyphus luke Seek mukundan), 60(Yuchen20), 60(Afordancja), 61(intgrah jimboko awu macaque sammyuri), 61(jonas ryno kg583 kabutack)
# lambda g:eval("[1.5*(x^y)for x,y in zip(g.pop(0),g[6])],"*6)
# ======================== 54 ========================
# lambda g:eval("[3/2*(x^y)for x,y in zip(g.pop(0),g[6])],"*6)
p=lambda g:[[3/2*(s.pop(0)^y)for y in g.pop(7)]for s in g[:6]]
