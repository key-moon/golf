# best: 70(luke, luke/sisyphus/Seek) / others: 72(ovs), 72(4atj), 72(att), 73(mukundan), 78(Seek64)
# ================================ 70 ================================
# p=lambda g:[*zip(*[[x and 9-sorted(map(sum,zip(*g))).index(sum(s))for x in s]for s in zip(*g)])]
p=lambda g:[*zip(*[[x and 9-sorted(zip(*g),key=sum).index(s)for x in s]for s in zip(*g)])]