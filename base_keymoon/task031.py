# best: 52(biz, luke, 4atj, sisyphus) / others: 54(att), 56(mukundan), 58(Seek64), 58(joking), 58(natte)
# 切り出し
# filter max で 0 の行を消してる 転地して列も同様に 最後にもっかい転置
# なんだけど、あと6 byte縮むらしい。一体どこで→bestはさらに2 byte縮んだらしい 意味不明
# p=lambda g,a=2:a and [*map(list,filter(max,zip(*p(g,a-1))))]or g
# 62
# E=lambda g:zip(*filter(max,g));p=lambda g:[[*r]for r in E(E(g))]
# E=lambda g:zip(*filter(max,g));p=lambda g:[*map(list,E(E(g)))]
# 61
# p=lambda g:[[*r]for r in zip(*filter(max,zip(*g)))if{*r}-{0}]
# 61
# p=lambda g:[*filter(max,map(list,zip(*filter(max,zip(*g)))))]
# 60
# p=lambda g:[[*r]for r in zip(*filter(max,zip(*g)))if max(r)]

# p=lambda g:[[c[0]for c in zip(r,*g)if max(c)]for r in g if max(r)]

# p=lambda g:max(min(g))and[*map(list,g)]or p([*zip(*filter(max,g))])
# p=lambda g,a=2:a and[*map(list,filter(max,zip(*p(g,a-1))))]or g
# ======================= 52 =======================
p=lambda g:[[*r]for r in zip(*filter(max,zip(*g)))if max(r)]
