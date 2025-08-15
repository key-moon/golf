A=range(10)
p=lambda g:[[g[0][max(i,j)%(4+(g[0][4]>0))]for j in A]for i in A]