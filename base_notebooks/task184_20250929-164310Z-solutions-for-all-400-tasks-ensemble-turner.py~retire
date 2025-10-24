def p(n):
 r=range;i,E=len(n),len(n[0]);B=[B for B in r(i)if all(n[B][r]==0for r in r(E))];C=[B for B in r(E)if all(n[r][B]==0for r in r(i))];B=[-1]+B+[i];C=[-1]+C+[E];G=[]
 for t in r(len(B)-1):
  F=[]
  for I in r(len(C)-1):
   for J in r(B[t]+1,B[t+1]):
    for i in r(C[I]+1,C[I+1]):
     if n[J][i]:F.append(n[J][i]);break
    else:continue
    break
  if F:G.append(F)
 return G
