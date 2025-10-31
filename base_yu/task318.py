# best: 54(Code Golf International, lv1.dev, jailctf merger, ox jam) / others: 58(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 58(4atj sisyphus luke Seek mukundan), 58(LogicLynx), 58(ALE-Agent), 58(santa2024)
# ======================== 54 ========================
# p=lambda g:[[x|y and 3for x,y in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:[[(x!=y)*3for x,y in zip(*c)]for c in zip(g,g[5:])]

# 00 0
# 01 3
# 20 3
# 21 3
