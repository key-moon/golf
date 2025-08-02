def p(g):
 A={}
 for F in g:
  for(C,B)in enumerate(F):
   if B:A.setdefault(B,[0,C])[0]+=1;A[B][1]=min(A[B][1],C)
 D=max(A[0]for A in A.values());E=[A for(A,B)in A.items()if B[0]==D];E.sort(key=lambda c:A[c][1]);return[E]*D