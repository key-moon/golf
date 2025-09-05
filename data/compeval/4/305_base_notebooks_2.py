def p(j):
 A=len(j)
 c=[x for r in j for x in r if x]
 if not c:return j
 E=sorted(set(c))
 k=len(E)
 W=[[0]*A for _ in[0]*A]
 for l in range(A):
  for J in range(A):W[l][J]=E[(l+J)%k]
 return W