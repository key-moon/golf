R=range
p=lambda g:[[g[i][j]or(10>(t:=9+all(g[i%4+6][i//4+5]==g[5-i//4][i%4+6]for i in R(2,20))-j)and g[t][i])*2for j in R(10)]for i in R(10)]