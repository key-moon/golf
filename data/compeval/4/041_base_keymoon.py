# best: 49(kg583, Seek64, luke, joking, 4atj, dbdr, kabutack, ovs, att, sisyphus) / others: 52(mukundan), 67(duckyluuk), 67(natte), 70(HashPanda), 84(MeWhenI)
# lambda g,a=0:[[(a:=a^c)|c for c in r]for r in g]
# ====================== 49 =====================
p=lambda g,a=0:[[c|(a:=a^c)for c in r]for r in g]
