def p(j,A=range(18)):
 for c in A:
  C,k,D=j[c:c+3]
  for l in A:
   B=l+3
   if sum(C[l:B]+k[l:B]+D[l:B])==0:C[l:B]=k[l:B]=D[l:B]=[1]*3
 return j