# best: 57(biz, luke, 4atj, att, sisyphus) / others: 62(mukundan), 62(Seek64), 62(joking), 62(xsot), 63(kg583)

# ========================== 57 =========================
# lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
# lambda g:[[[*{0,*sum(g,[])}-{v,v-5}][0]for v in s]for s in g]
p=lambda g:[[[*{*sum(g,[])}-{v},0][v!=5]for v in r]for r in g]

