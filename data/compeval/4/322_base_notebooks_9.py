def p(m,v=range):
 for c in v(len(m[0])):
  for r in v(len(m)):
   if m[r][c]:break
  else:continue
  for i in v(r,len(m)):m[i][c]=m[r][c]
 return m