def p(g):
 i=sum(g,[]).index(2);x,y=divmod(i,5);g[x][y]=0
 if x*y:g[x-1][y-1]=3
 if x<2and y:g[x+1][y-1]=8
 if y<4and x:g[x-1][y+1]=6
 if x<2and y<4:g[x+1][y+1]=7
 return g
