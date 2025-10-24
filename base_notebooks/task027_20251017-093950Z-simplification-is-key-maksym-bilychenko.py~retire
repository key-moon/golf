def p(r,e=enumerate):
 c=eval(str(r));H=len(r);a={(i,q)for i,R in e(r)for q,v in e(R)if v}
 if not a:return c
 for l in(0,1):
  E={X for i,q in a for X in[(5-i+l,q-5),(5-q+l,4-i+l),(i-5,q-4)]}
  if(P:=[(i,q)for i,q in E if{(5-i+l,5+q),(4-q+l,5-i+l),(5+q,4+i)}<=a])and({z for i,q in P for z in[(5-i+l,5+q),(5+q,4+i)]}|{(4-q+l,5-i+l)for i,q in P if 0<=4-q+l<H})==a:
   for i,q in P:
    if 0<=4+i<H and not c[4+i][4-q+l]:c[4+i][4-q+l]=2
 return c