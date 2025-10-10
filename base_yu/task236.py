# best: 54(jailctf merger, ox jam) / others: 60(jacekw Potatoman nauti natte), 60(4atj sisyphus luke Seek mukundan), 60(intgrah jimboko awu macaque sammyuri), 61(biz), 62(cubbus)
# ======================== 54 ========================
# lambda g:[[sum(a)*1.5%2//1for a in zip(*c)]for c in zip(g,g[5:])]
# lambda g:[[3*(x^y//2)for x,y in zip(*c)]for c in zip(g,g[5:])]
# lambda g:eval("[3*(x^y//2)for x,y in zip(g.pop(0),g[4])],"*4)
# lambda g:eval("[x*3^-y%5for x,y in zip(g.pop(0),g[4])],"*4)
p=lambda g:eval("[x*3^-y%5for x,y in zip(g.pop(0),g[4])],"*4)


# 00 0
# 01 3
# 20 3
# 21 0
