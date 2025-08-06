R=range(10)
p=lambda g:[[g[0][max(i,j)%(4+(g[0][4]>0))]for j in R]for i in R]

# def p(g):
#  return[[g[0][max(i,j)%(4+(g[0][4]>0))] for j in range(10)]for i in range(10)]