def p(j,A=range):
 c=len(j);E=len(j[0]);k=len({*sum(j,[])}-{0})
 j=[[j[l//k][J//k]for J in A(E*k)]for l in A(c*k)];c*=k;E*=k
 for W in A(min(c,E),0,-1):
  for l in A(c-W+1):
   for J in A(E-W+1):
    a=j[l][J]
    if a and all(r[J:J+W]==[a]*W for r in j[l:l+W]):
     for C,e in(-1,-1),(-1,W),(W,-1),(W,W):
      K=l+C;w=J+e
      while-1<K<c and-1<w<E and not j[K][w]:j[K][w]=2;K+=C>0 or-1;w+=e>0 or-1
     return j