def p(m,F=range):
 for c in F(len(m[0])):
  for r in F(len(m)):
   if m[r][c]:break
  else:continue
  for i in F(r,len(m)):m[i][c]=m[r][c]
 return m