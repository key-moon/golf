def p(m):
 R,C=len(m),len(m[0])
 D,O={},[r[:]for r in m]
 for r in range(R):
  for c in range(C):
   v=m[r][c]
   if v:D.setdefault(v,[]).append((r,c))
 for v in D:
  (y1,x1),(y2,x2)=D[v]
  dy=1if y2>y1 else-1
  dx=1if x2>x1 else-1
  for i in range(abs(y2-y1)+1):O[y1+i*dy][x1+i*dx]=v
 return O

