# best: 54
# 切り出し
# filter max で 0 の行を消してる 転地して列も同様に 最後にもっかい転置
# なんだけど、あと6 byte縮むらしい。一体どこで
# 62
# E=lambda g:zip(*filter(max,g))
# p=lambda g:[*map(list,E(E(g)))]
# p=lambda g:[[*r]for r in E(E(g))]
# 61
# p=lambda g:[[*r]for r in zip(*filter(max,zip(*g)))if{*r}-{0}]
# 60
# p=lambda g:[*filter(max,map(list,zip(*filter(max,zip(*g)))))]
# 60
p=lambda g:[[*r]for r in zip(*filter(max,zip(*g)))if max(r)]
