# 類題:180
# best: 81(luke) / others: 82(mukundan), 82(sisyphus), 83(kabutack), 84(natte), 84(att)
# ====================================== 81 =====================================
# lambda g:[[g[i][j]or g[i][j+5]or g[i+5][j]or g[i+5][j+5] for j in range(4)]for i in range(4)]
# lambda g,R=range(4):[[g[i][j]or g[i][j+5]or g[i+5][j]or g[i+5][j+5] for j in R]for i in R]
# lambda g:[[s[j]or s[j+5]or t[j]or t[j+5] for j in range(4)]for s,t in zip(g,g[5:])]
# lambda g:[[s[j]or s[j+5]or t[j]or t[j+5] for j in(0,1,2,3)]for s,t in zip(g,g[5:])]
# lambda g:[[s[j-5]or s[j]or t[j-5]or t[j]for j in b""]for s,t in zip(g,g[5:])]
p=lambda g:[[max(s[j::5])or max(t[j::5])for j in(0,1,2,3)]for s,t in zip(g,g[5:])]

#  b"\0123"
# (0,1,2,3)

# 値
# 7 4
# 8 6
# 順序
# 1 2
# 3 4
