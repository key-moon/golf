def p(j,A=range):
 c,E=len(j),len(j[0])
 k,W={},[l[:]for l in j]
 for l in A(c):
  for J in A(E):
   a=j[l][J]
   if a:k.setdefault(a,[]).append((l,J))
 for a in k:
  (p,C),(e,K)=k[a]
  w=1if e>p else-1
  L=1if K>C else-1
  for b in A(abs(e-p)+1):W[p+b*w][C+b*L]=a
 return W