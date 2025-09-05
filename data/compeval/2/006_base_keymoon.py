# best: 51(mukundan, luke, 4atj, ovs, att, sisyphus) / others: 53(kg583), 53(cg), 53(Seek64), 53(HashPanda), 53(biz)
#  b"012"
# (0,1,2)
# sum(r[i::4])
# r[i]+r[i+4]
# ======================= 51 ======================
p=lambda g:[[2*all(r[i::4])for i in(0,1,2)]for r in g]
