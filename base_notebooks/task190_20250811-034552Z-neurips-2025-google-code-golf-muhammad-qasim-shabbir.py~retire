def p(j):
 A=range
 c=[a[:]for a in j]
 E=[(0,1),(1,0),(0,-1),(-1,0)]
 k=[(-1,-1),(-1,1),(1,1),(1,-1)]
 for W in A(10):
  for l in A(10):
   if j[W][l]and all(0<=W+a<10and 0<=l+C<10and j[W+a][l+C]==0for a,C in E):
    for J in k:
     a,C=W+J[0],l+J[1]
     if 0<=a<10and 0<=C<10and j[a][C]:
      e,K=-J[0],-J[1]
      for w in A(1,10):
       L,b=W+e*w,l+K*w
       if 0<=L<10and 0<=b<10:c[L][b]=j[W][l]
 return c