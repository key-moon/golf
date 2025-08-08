def p(g):
 X=[]
 Z=[]
 E=enumerate
 for r,R in E(g):
  if 1 in R:X.append([1 for _ in R])
  elif 3 in R:X.append([3 for _ in R])
  else:X.append(R[:])
  for c,C in E(R):
   if C==2:Z.append(c)
 for r,R in E(X):
  for c,C in E(R):
   if c in Z and C==0:X[r][c]=2
 return X