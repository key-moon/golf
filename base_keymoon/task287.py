# best: 63
# 78
# r=range(16)
# p=lambda g:[[({g[i][j],g[~i][~j]}-{4}).pop() for j in r] for i in r]
# 76
# E=enumerate
# p=lambda g:[[[c,g[~i][~j]][c==4] for j,c in E(r)] for i,r in E(g)]
# 73
p=lambda g:[[a[a[0]==4]for a in zip(a,b[::-1])]for a,b in zip(g,g[::-1])]