# best: 54(jailctf merger) / others: 60(4atj sisyphus luke Seek mukundan), 61(intgrah jimboko awu macaque sammyuri), 61(xsot ovs att joking mewheni), 63(jonas ryno kg583), 63(JRK)
# ======================== 54 ========================
# lambda g:[[sum(a)*1.5%2//1for a in zip(*c)]for c in zip(g,g[5:])]
# p=lambda g:[[3*(x^y//2)for x,y in zip(*c)]for c in zip(g,g[5:])]
# p=lambda g:eval("[3*(x^y//2)for x,y in zip(g.pop(0),g[4])],"*4)
p=lambda g:eval("[x*3^-y%5for x,y in zip(g.pop(0),g[4])],"*4)

# 00 0
# 01 3
# 20 3
# 21 0

