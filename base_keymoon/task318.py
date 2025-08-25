# best: 60(biz) / others: 61(kg583), 61(luke), 61(att), 61(sisyphus), 62(mukundan)
# =========================== 60 ===========================
# lambda g:[[any(a)*3for a in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:eval("[any(a)*3for a in zip(g.pop(0),g[4])],"*4)
