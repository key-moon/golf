A=range
p=lambda g:[[g[i%5][j%6]for j in A(len(g[0])*2)]for i in A(len(g)*1)]