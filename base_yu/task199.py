# best: 101(luke/sisyphus/Seek) / others: 102(joking+MWI), 102(joking/MWI), 104(kg583), 107(MeWhenI), 112(mukundan)
# =============================================== 101 ===============================================
# p=lambda g:(l:=[*map(max,*g)])and[([4,0]*9)[l.index(max(l))%2:][:len(g)]]*-~(k:=g.index(l))+g[k:-1]
# p=lambda g:[[t:=(l:=[*map(max,*g)]).index(max(l))%2*4]*0+[(t:=4-t)for _ in g]]*-~(k:=g.index(l))+g[k:-1]
p=lambda g:[([4,0]*9)[(l:=[*map(max,*g)]).index(max(l))%2:][:len(g)]]*-~(k:=g.index(l))+g[k:-1]
