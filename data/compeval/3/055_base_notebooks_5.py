def p(j,A=range):
 c,E=len(j),len(j[0])
 k=[a[:]for a in j]
 W,l=[a for a in A(c)if all(v==8 for v in j[a])]
 p,J=[C for C in A(E)if all(j[a][C]==8 for a in A(c))]
 for a in A(c):
  for C in A(E):
   if not k[a][C]:
    if a<W and p<C<J:k[a][C]=2
    elif W<a<l and C<p:k[a][C]=4
    elif W<a<l and p<C<J:k[a][C]=6
    elif W<a<l and C>J:k[a][C]=3
    elif a>l and p<C<J:k[a][C]=1
 return k