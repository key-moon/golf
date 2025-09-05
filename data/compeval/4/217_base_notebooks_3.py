def p(g,R=range(9)):a,b=next(i for i,r in enumerate(g)if sum(r))//3*3,next(i for i in R if sum(g[y][i]for y in R))//3*3;return[[g[a+y%3][b+x%3]*bool(g[a+y//3][b+x//3])for x in R]for y in R]
