# 多分かなり短い
p=lambda g:[sum((g[i%3]if g[i//3][j]else[0]*3 for j in(0,1,2)),[])for i in range(9)]