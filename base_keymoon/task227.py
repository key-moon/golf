# best: 52(jailctf merger) / others: 55(4atj sisyphus luke Seek mukundan), 55(4atj sisyphus luke Seek), 55(xsot ovs att joking mewheni), 57(mukundan), 61(kg583)
# lambda g:[*eval("[2*(x+y<1)for x,y in zip(g.pop(0),g[3])],"*4)]
# lambda g:[*eval("[2-2*any(a)for a in zip(g.pop(0),g[3])],"*4)]
# lambda g:[[2*~a&2for a in map(max,*c)]for c in zip(g,g[4:])]
# lambda g:[[2-any(a)*2for a in zip(*c)]for c in zip(g,g[4:])]
# lambda g:eval("[2-2*any(a)for a in zip(g.pop(0),g[3])],"*4)
# lambda g:eval("[~-any(a)%3for a in zip(g.pop(0),g[3])],"*4)
# lambda g:eval("[2*~a&2for a in map(max,g.pop(0),g[3])],"*4)
# ======================= 52 =======================
p=lambda g:[[2*~a&2for a in map(max,g.pop(4),s)] for s in g]

# mapping = { 0: 2, 1: 0, 3: 0 }
