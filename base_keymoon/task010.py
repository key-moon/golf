# best: 70(luke/sisyphus/Seek, luke) / others: 72(4atj), 72(ovs), 72(att), 73(mukundan), 78(Seek64)
# lambda g:[*zip(*[[(9-sorted(zip(*g)).index(r))*(0<c)for c in r]for r in zip(*g)])]
# ================================ 70 ================================
# lambda g:[*zip(*[[(9-sorted(zip(*g)).index(r))*c/5for c in r]for r in zip(*g)])]
# lambda g:[[(9-sorted(zip(*g)).index(t[1:]))*t[0]/5for t in zip(r,*g)]for r in g]
# lambda g:[[(9-sorted(zip(*g)).index(t))*c/5for c,t in zip(r,zip(*g))]for r in g]
# lambda g:[[(9-sorted(zip(*g)).index((*t,)))*c/5for*t,c in zip(*g,r)]for r in g]
p=lambda g:[[(9-sorted(zip(*g,r)).index(t))*t[9]/5for t in zip(*g,r)]for r in g]
