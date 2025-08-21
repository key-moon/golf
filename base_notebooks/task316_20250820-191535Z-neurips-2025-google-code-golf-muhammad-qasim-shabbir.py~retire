def p(m,u=range):
 n=3
 v=[]
 for c in u(len(m[0])):
  for r in u(len(m)):
   if m[r][c]:v.append(m[r][c]);break
 v.extend([0]*(n*n-len(v)))
 return[v[i*n:(i+1)*n]if i%2==0 else v[i*n:(i+1)*n][::-1]for i in u(n)]