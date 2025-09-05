# best: 57(luke, 4atj, att, biz, sisyphus) / others: 62(mukundan), 62(Seek64), 62(joking), 62(xsot), 63(ovs)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]