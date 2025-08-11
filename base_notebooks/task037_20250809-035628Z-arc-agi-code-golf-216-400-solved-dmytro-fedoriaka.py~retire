def p(m,S=range):
 R,C=len(m),len(m[0])
 D,O={},[r[:]for r in m]
 for r in S(R):
  for c in S(C):
   v=m[r][c]
   if v:D.setdefault(v,[]).append((r,c))
 for v in D:
  (p,U),(y,j)=D[v]
  Y=1if y>p else-1
  P=1if j>U else-1
  for i in S(abs(y-p)+1):O[p+i*Y][U+i*P]=v
 return O