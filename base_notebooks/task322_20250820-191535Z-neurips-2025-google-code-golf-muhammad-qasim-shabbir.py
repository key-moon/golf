def p(m,u=range):
 for c in u(len(m[0])):
  for r in u(len(m)):
   if m[r][c]:break
  else:continue
  for i in u(r,len(m)):m[i][c]=m[r][c]
 return m