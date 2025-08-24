# best: 60(4atj) / others: 61(luke), 62(mukundan), 62(Seek64), 62(sisyphus), 63(kg583)
# lambda g:[[sum(a)*1.5%2//1for a in zip(*c)]for c in zip(g,g[5:])]
# =========================== 60 ===========================
# p=lambda g:[[3*(x^y//2)for x,y in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:eval("[3*(x^y//2)for x,y in zip(g.pop(0),g[4])],"*4)

# 00 0
# 01 3
# 20 3
# 21 0
