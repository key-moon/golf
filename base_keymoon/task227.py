# 類題: 347 006 5 byte多い
# best: 55(4atj) / others: 57(mukundan), 57(luke), 58(att), 60(Seek64), 60(ovs)
# lambda g:[*eval("[2*(x+y<1)for x,y in zip(g.pop(0),g[3])],"*4)]
# ========================= 55 ========================
p=lambda g:[*eval("[2-2*any(a)for a in zip(g.pop(0),g[3])],"*4)]
