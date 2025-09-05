# best: 47(luke, att) / others: 48(mukundan), 48(duckyluuk), 48(ovs), 48(natte), 48(sisyphus)
# lambda g:[[0]*len(g),*eval(str(g).replace(*"82"))[:-1]]
# lambda g:eval(str(g*2).replace(*"82"))[len(g)-1:-1]
# lambda g:[g[-1],*eval(str(g).replace(*"82"))[:-1]]
# lambda g:[g[-1]]+eval(str(g).replace(*"82"))[:-1]
# lambda g:g[-1:]+eval(str(g).replace(*"82"))[:-1]
# lambda g:g[-1:]+eval(str(g).replace(*"82"))[:-1]
# ===================== 47 ====================
p=lambda g:[[c/4for c in r]for r in[g.pop()]+g]
