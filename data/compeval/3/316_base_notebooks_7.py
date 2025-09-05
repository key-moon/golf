def p(m):
 n,v=3,[]
 for c in range(len(m[0])):
  for r in range(len(m)):
   if m[r][c]:
    v.append(m[r][c])
    break
 v.extend([0]*(n*n-len(v)))
 return [v[i*n:(i+1)*n] if i%2==0 else v[i*n:(i+1)*n][::-1] for i in range(n)]
