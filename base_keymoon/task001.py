# 多分かなり短い
p=lambda g:[sum(([[0]*3,g[i%3]][g[i//3][j]>0]for j in(0,1,2)),[])for i in range(9)]