# best: 54(jailctf merger) / others: 60(4atj sisyphus luke Seek), 62(xsot ovs att joking mewheni), 62(mukundan), 63(kg583), 65(natte)
# ======================== 54 ========================
# lambda g:[[sum(a)*1.5%2//1for a in zip(*c)]for c in zip(g,g[5:])]
# p=lambda g:[[3*(x^y//2)for x,y in zip(*c)]for c in zip(g,g[5:])]
# p=lambda g:eval("[3*(x^y//2)for x,y in zip(g.pop(0),g[4])],"*4)
p=lambda g:eval("[x*3^-y%5for x,y in zip(g.pop(0),g[4])],"*4)

# 00 0
# 01 3
# 20 3
# 21 0
