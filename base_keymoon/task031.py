# best: 45(4atj sisyphus luke Seek, sisyphus) / others: 47(luke), 47(xsot ovs att), 47(att), 49(joking MeWhenI), 50(kg583)
# ==================== 45 ===================
# 類題: 57
# 切り出し
# filter max で 0 の行を消してる 転地して列も同様に 最後にもっかい転置
# なんだけど、あと6 byte縮むらしい。一体どこで→bestはさらに2 byte縮んだらしい 意味不明
# p=lambda g:[[c[0]for c in zip(r,*g)if max(c)]for r in g if max(r)]
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
# lambda g,c=-63:g*c or p([*zip(*g[-2+any(g[-1])::-1])],c+1)

# lambda g:max(min(g))and g or p([*zip(*filter(max,g))])
# lambda g:[p,list][type(g)!=list](filter(max,zip(*g)))
# lambda g,a=2:a and[*filter(max,zip(*p(g,a-1)))]or g
# lambda g:[p,list][g*0!=[]]((*filter(max,zip(*g)),))
# lambda g,E=lambda g:zip(*filter(max,g)):[*E(E(g))]
# lambda g,c=-1:g*c or[*zip(*filter(max,p(g,c+1)))]
# lambda g,F=filter:[*F(max,zip(*F(max,zip(*g))))]
# best: 45(4atj sisyphus luke Seek, sisyphus) / others: 47(luke), 47(att), 50(kabutack), 52(biz), 52(4atj)
# ==================== 45 ===================
p=lambda g:g*any(g[0])or (DUMP("kasu")and DUMP(p([*zip(*filter(max,g))])))
