p=lambda g,X=range(9):[[g[r//3][c//3]&g[r%3][c%3]for c in X]for r in X]
# p=lambda g:[sum(([[0]*3,g[i%3]][g[i//3][j]>0]for j in(0,1,2)),[])for i in range(9)]
