# p=lambda g,R=range(16):[*filter(len,[[g[15-i][15-j]for j in R if g[i][j]==3]for i in R])]
p=lambda g,R=range(16):[u for i in R if(u:=[g[15-i][15-j]for j in R if g[i][j]==3])]
# p=lambda g,R=range(16):[u for x,y in zip(g,g[::-1]) if(u:=[w for v,w in zip(x,y[::-1]) if v==3])]