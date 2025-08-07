R=range
def p(g):
 for y in R(-20,20):
  for x in R(-20,20):
   if~-any((g[i][j]!=g[i-y][j-x])*g[i][j]*g[i-y][j-x]for i in R(29)for j in R(29)if(i-y<29)*(j-x<29)):
    for I in R(841):
     if-1<(i:=I%29)-y<29and-1<(j:=I//29)-x<29:
      s,t=g[i-y],g[i]
      s[j-x]=s[j-x]or t[j]
      t[j]=t[j]or s[j-x]
 return g

# def p(g):
#  for y in range(-20,20):
#   for x in range(-20,20):
#    if 1-any(g[i][j]!=g[i-y][j-x]and g[i][j]and g[i-y][j-x]for i in range(y,29) for j in range(29) if i-y<29 and 0<=j-x<29):
#     for i in range(29):
#      for j in range(29):
#       if-1<i-y<29 and-1<j-x<29:
#        if g[i-y][j-x]<1:g[i-y][j-x]=g[i][j]
#        if g[i][j]<1:g[i][j]=g[i-y][j-x]
#  return g