# best: 59(luke, 4atj, att, sisyphus) / others: 61(joking+MWI), 61(kg583), 61(mukundan), 61(Seek64), 61(joking)
# lambda g:[eval("(a.pop(0)+b.pop(0)<1)*3,"*4)for a,b in zip(g,g[5:])]
# =========================== 59 ==========================
p=lambda g:eval("[3-any(a)*3for a in zip(g.pop(0),g[4])],"*4)
