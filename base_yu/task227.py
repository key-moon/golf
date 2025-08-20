# best: 55(4atj) / others: 57(luke), 57(mukundan), 58(att), 60(ovs), 60(Seek64)
# ========================= 55 ========================
# p=lambda g:[[2-2*(x|y>0)for x,y in zip(*c)]for c in zip(g,g[4:])]
# p=lambda g:[*eval("[2-2*(x|y>0)for x,y in zip(g.pop(0),g[3])],"*4)]
p=lambda g:[*eval("[2*(x+y<1)for x,y in zip(g.pop(0),g[3])],"*4)]
# p=lambda g:[[2*(g[i][j]==g[i+4][j]<1)for j in range(4)]for i in range(4)]
