# best: 55(4atj) / others: 57(mukundan), 57(luke), 58(att), 60(Seek64), 60(ovs)
# lambda g:[*eval("[2*(x+y<1)for x,y in zip(g.pop(0),g[3])],"*4)]
# lambda g:[*eval("[2-2*any(a)for a in zip(g.pop(0),g[3])],"*4)]
# lambda g:[[2*~a&2for a in map(max,*c)]for c in zip(g,g[4:])]
# lambda g:[[2-any(a)*2for a in zip(*c)]for c in zip(g,g[4:])]
# { 0: 1, 3: 0 }
# lambda g:eval("[2-2*any(a)for a in zip(g.pop(0),g[3])],"*4)
# lambda g:eval("[~-any(a)%3for a in zip(g.pop(0),g[3])],"*4)
# { 0: 2, 3: 0 }
# lambda g:eval("[2*~a&2for a in map(max,g.pop(0),g[3])],"*4)
# ========================= 55 ========================
p=lambda g:eval("[2*~a&2for a in map(max,g.pop(0),g[3])],"*4)
