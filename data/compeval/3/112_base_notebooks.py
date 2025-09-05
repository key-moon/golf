def p(j,p=enumerate):
 A=c=0
 for E,k in p(j):
  for W,l in p(k):A+=E*(l==3);c+=W*(l==3)
 A//=2;c//=2
 for E,k in p(j):
  for W,l in p(k):
   if l==2:
    for J,a in(E,W),(A-E,W),(E,c-W),(A-E,c-W):j[J][a]=2
 return j