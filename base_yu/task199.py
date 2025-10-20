# best: 84(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, biz) / others: 87(ox jam), 90(THUNDER THUNDER), 102(jacekwl Potatoman nauti), 102(jacekw Potatoman nauti natte), 102(jacekw Potatoman nauti)
# ======================================= 84 =======================================
# p=lambda g:(l:=[*map(max,*g)])and[([4,0]*9)[l.index(max(l))%2:][:len(g)]]*-~(k:=g.index(l))+g[k:-1]
# p=lambda g:[[t:=(l:=[*map(max,*g)]).index(max(l))%2*4]*0+[(t:=4-t)for _ in g]]*-~(k:=g.index(l))+g[k:-1]
# p=lambda g:[([4,0]*9)[(l:=max(g)).index(max(l))%2:][:len(g)]]*-~(k:=g.index(l))+g[k:-1]
p=lambda g:[([0,4]*9)[any(max(g)[::2]):][:len(g)]]*-~(k:=g.index(max(g)))+g[k:-1]
