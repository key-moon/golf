def p(m,k=range):
 for c in k(len(m[0])):
  for r in k(len(m)):
   if m[r][c]:break
  else:continue
  for i in k(r,len(m)):m[i][c]=m[r][c]
 return m