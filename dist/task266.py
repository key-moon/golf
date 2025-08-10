def p(j):
 B=sum(j,[]).index(2);c,A=divmod(B,5);j[c][A]=0
 if c*A:j[c-1][A-1]=3
 if c<2and A:j[c+1][A-1]=8
 if A<4and c:j[c-1][A+1]=6
 if c<2and A<4:j[c+1][A+1]=7
 return j