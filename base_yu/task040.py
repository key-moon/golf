# =========================== best 73 by 4atj ===========================
# p=lambda g:[[g[i][j]and g[i>4 and 9][j>4 and 9]for j in range(10)]for i in range(10)]
# p=lambda g,E=enumerate:[[v and g[(i>4)*9][(j>4)*9]for j,v in E(s)]for i,s in E(g)]
# p=lambda g,R=range(10):[[g[i][j]and g[i>4and 9][j>4and 9]for j in R]for i in R]
# p=lambda g,R=range(10):[[g[i][j]and g[(i>4)*9][(j>4)*9]for j in R]for i in R]
p=lambda g,R=range(10):[[g[i][j]and g[-(i>4)][-(j>4)]for j in R]for i in R]