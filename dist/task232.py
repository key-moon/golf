def p(g):
 for C in g:
  try:A,D=next((i,v)for i,v in enumerate(C)if v)
  except:continue
  for B in range(len(C)-A):C[A+B]=[D,5][B&1]
 return g