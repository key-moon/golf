def p(g):
 X=[]
 T=[]
 for R in g:
  if max(R)>0:X.append(R)
 for R in X:
  for i in range(len(R)):
     if R[i]>0:T.append(i)
 X=[R[min(T):max(T)+1]for R in X]
 X=[R*2 for R in X]
 return X