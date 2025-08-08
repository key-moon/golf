A=range
def p(g):return[[g[i][j]or g[i][j+5]or g[i+5][j]or g[i+5][j+5]for j in A(4)]for i in A(4)]