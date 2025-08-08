def p(g):
 R=range
 n,m=len(g),len(g[0])
 v=[]
 for i in R(n):
  if i==0 or g[i]!=g[i-1]:
   v.append([g[i][0]])
 h=[]
 p=-1
 for j in R(m):
  if j==0 or any(g[i][j]!=g[i][j-1]for i in R(n)):
   h.append(g[0][j])
 if len(v)>1:
  return v
 else:
  return [h]