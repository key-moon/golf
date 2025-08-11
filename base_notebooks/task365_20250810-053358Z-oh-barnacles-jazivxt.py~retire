def p(j):
 A,c=len(j),len(j[0]);E=-1
 for k in range(A):
  for W in range(c):
   if j[k][W]and(k<1or j[k-1][W]<1)and(W<1or j[k][W-1]<1):
    l=J=1
    while W+l<c and j[k][W+l]:l+=1
    while k+J<A and j[k+J][W]:J+=1
    a=[C[W:W+l]for C in j[k:k+J]]
    C=sum(z.count(2)for z in a)
    if C>E:E=C;e=a
 return e
