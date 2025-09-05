# best: 57(biz, luke, 4atj, att, sisyphus) / others: 62(mukundan), 62(Seek64), 62(joking), 62(xsot), 63(kg583)

# {*sum(g,[])}
# {*g[0]+g[1]}
# ========================== 57 =========================
# lambda g:[[[*{*sum(g,[])}-{5}][0]*(v==5)for v in r]for r in g]
# lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
# lambda g:[[[*{0,*sum(g,[])}-{v,v-5}][0]for v in s]for s in g]
# lambda g:[[(sum({*sum(g,[])})-5)*(v==5)for v in r]for r in g]
# lambda g:[[sum({*sum(g,[])}-{5})*(v==5)for v in r]for r in g]
# lambda g:[[sum({*sum(g*(v==5),[])}-{5})for v in r]for r in g]
# lambda g:[[[*{*sum(g,[])}-{v},0][v!=5]for v in r]for r in g]
p=lambda g:[[sum({*sum(g,[-5])})*(v==5)for v in r]for r in g]