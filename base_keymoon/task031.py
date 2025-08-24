# best: 52(biz, luke, 4atj, sisyphus) / others: 54(att), 56(mukundan), 58(Seek64), 58(joking), 58(natte)
# best: 47(att) / others: 52(biz), 52(luke), 52(4atj), 52(sisyphus), 56(mukundan)
# 類題: 57
# 切り出し
# filter max で 0 の行を消してる 転地して列も同様に 最後にもっかい転置
# なんだけど、あと6 byte縮むらしい。一体どこで→bestはさらに2 byte縮んだらしい 意味不明
# p=lambda g:[[c[0]for c in zip(r,*g)if max(c)]for r in g if max(r)]
# p=lambda g,a=2:a and [*map(list,filter(max,zip(*p(g,a-1))))]or g
# 62
# E=lambda g:zip(*filter(max,g));p=lambda g:[[*r]for r in E(E(g))]
# E=lambda g:zip(*filter(max,g));p=lambda g:[*map(list,E(E(g)))]
# 61
# p=lambda g:[[*r]for r in zip(*filter(max,zip(*g)))if{*r}-{0}]
# 61
# lambda g:[*filter(max,map(list,zip(*filter(max,zip(*g)))))]
# 60
# lambda g:[[*r]for r in zip(*filter(max,zip(*g)))if max(r)]

# lambda g:max(min(g))and g or p([*zip(*filter(max,g))])
# lambda g:[p,list][type(g)!=list](filter(max,zip(*g)))
# lambda g,a=2:a and[*filter(max,zip(*p(g,a-1)))]or g
# lambda g:[p,list][g*0!=[]]((*filter(max,zip(*g)),))
# lambda g,E=lambda g:zip(*filter(max,g)):[*E(E(g))]
# lambda g,c=-1:g*c or p([*zip(*filter(max,g))],c+1)
# lambda g,F=filter:[*F(max,zip(*F(max,zip(*g))))]
# ===================== 47 ====================
p=lambda g:g*any(g[0])or p([*zip(*filter(max,g))])


