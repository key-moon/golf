def p(grid):
 n=len(grid)
 output=[[0 for _ in range(n)]for _ in range(n)]
 for i in range(n):
  for j in range(n):
   if grid[i][j]==5:
    for x in range(max(0, i-1), min(n, i+2)):
     for y in range(max(0, j-1), min(n, j+2)):
      output[x][y]=1
 return output