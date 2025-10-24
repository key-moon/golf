e=enumerate
def p(j):
 f=u=0
 for i,r in e(j):
  for o,g in e(r):f+=i*(g==3);u+=o*(g==3)
 f>>=1;u>>=1
 for i,r in e(j):
  for o,g in e(r):
   if g==2:r[o]=j[f-i][o]=j[i][u-o]=j[f-i][u-o]=2
 return j