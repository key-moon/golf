# best: 56(luke, sisyphus) / others: 58(ovs), 60(joking), 61(mukundan), 61(duckyluuk), 62(MeWhenI)
# ========================= 56 =========================
# p=lambda g:[[v+2*(v>0)*(i%3<1)for i,v in enumerate(s)]for s in g]
p=lambda g:[[v*1.5**(i%3<1)for i,v in enumerate(s)]for s in g]