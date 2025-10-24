def p(e,i=len,b=range):
 p,p=i(e),i(e[0]);r,l=0,[]
 for m in b(i(e)):
  d=[e[m][0]]
  for h in b(i(e[m])-1):
   if e[m][h+1]!=e[m][h]:d+=[e[m][h+1]]
  if i(d)>r:r=i(d);l=d[:]
 e=[l[:]for m in b(i(l))]
 for m in b(i(e)//2):
  for r in b(m,i(e[0])-m-1):e[m][r]=e[m][m];e[-(m+1)][r]=e[-(m+1)][m]
 return e