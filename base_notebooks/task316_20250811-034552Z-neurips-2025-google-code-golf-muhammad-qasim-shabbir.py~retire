def p(m,D=range):
 n=3
 v=[]
 for c in D(len(m[0])):
  for r in D(len(m)):
   if m[r][c]:v.append(m[r][c]);break
 v.extend([0]*(n*n-len(v)))
 return[v[i*n:(i+1)*n]if i%2==0 else v[i*n:(i+1)*n][::-1]for i in D(n)]