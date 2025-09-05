# 類題:257
# best: 79(luke, luke/sisyphus/Seek) / others: 82(ovs), 82(mukundan), 82(4atj), 82(sisyphus), 84(dbdr)
# ===================================== 79 ====================================
# p=lambda g:[[s[j+4]or t[j]or t[j+4]or s[j] for j in(0,1,2,3)]for s,t in zip(g,g[4:])]
p=lambda g:[[s[j]or t[j-4]or t[j]or s[j-4]for j in b""]for s,t in zip(g,g[4:])]

# 値
# 4 5
# 6 7
# 順序
# 4 1
# 2 3
