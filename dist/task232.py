def p(g):
 for AC in g:
  try:AA,AD=next((i,v)for i,v in enumerate(AC)if v)
  except:continue
  for AB in range(len(AC)-AA):AC[AA+AB]=[AD,5][AB&1]
 return g