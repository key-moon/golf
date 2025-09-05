p=lambda g:[[2 if g[i][j]==5 and all(0<=i+d[0]<10 and 0<=j+d[1]<10 and g[i+d[0]][j+d[1]]==5 for d in [(-1,0),(1,0),(0,-1),(0,1)]) else g[i][j] for j in range(10)] for i in range(10)]
