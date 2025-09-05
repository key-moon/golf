# best: 60(biz) / others: 61(luke), 61(att), 61(kg583), 61(sisyphus), 62(mukundan)
# =========================== 60 ===========================
# p=lambda g:[[x|y and 3for x,y in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:[[(x!=y)*3for x,y in zip(*c)]for c in zip(g,g[5:])]

# 00 0
# 01 3
# 20 3
# 21 3
