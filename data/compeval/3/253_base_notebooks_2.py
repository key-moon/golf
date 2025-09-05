def p(g):
 n=len(g)-1;A=[0]*16
 for i in range(n):
  for j in range(n):
   if(c:=g[i][j])and g[i+1][j]==c and g[i][j+1]==c:A[0]=A[4]=A[1]=c
   if c and g[i+1][j]==c and g[i+1][j+1]==c:A[8]=A[12]=A[13]=c
   if c and g[i][j+1]==c and g[i+1][j+1]==c:A[2]=A[3]=A[7]=c
   if(d:=g[i+1][j+1])and g[i+1][j]==d and g[i][j+1]==d:A[11]=A[14]=A[15]=d
 return[A[i:i+4]for i in(0,4,8,12)]