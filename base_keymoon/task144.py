# best: 53(jailctf merger) / others: 59(4atj sisyphus luke Seek mukundan), 59(intgrah jimboko awu macaque sammyuri), 59(xsot ovs att joking mewheni), 61(jonas ryno kg583), 61(JRK)
# lambda g:[eval("(a.pop(0)+b.pop(0)<1)*3,"*4)for a,b in zip(g,g[5:])]
# ======================== 53 =======================
p=lambda g:eval("[3-any(a)*3for a in zip(g.pop(0),g[4])],"*4)
