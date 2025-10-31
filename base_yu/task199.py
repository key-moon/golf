# best: 77(lv1.dev, LogicLynx, FuunAgent) / others: 79(Code Golf International), 79(ALE-Agent), 81(HIMAGINE THE FUTURE.), 81(biz), 82(Ravi Annaswamy)
# ==================================== 77 ===================================
# p=lambda g:(l:=[*map(max,*g)])and[([4,0]*9)[l.index(max(l))%2:][:len(g)]]*-~(k:=g.index(l))+g[k:-1]
# p=lambda g:[[t:=(l:=[*map(max,*g)]).index(max(l))%2*4]*0+[(t:=4-t)for _ in g]]*-~(k:=g.index(l))+g[k:-1]
# p=lambda g:[([4,0]*9)[(l:=max(g)).index(max(l))%2:][:len(g)]]*-~(k:=g.index(l))+g[k:-1]
p=lambda g:[([0,4]*9)[any(max(g)[::2]):][:len(g)]]*-~(k:=g.index(max(g)))+g[k:-1]
