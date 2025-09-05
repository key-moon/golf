j=lambda A,c,E:[[c if i==E else E for i in r]for r in A]
def p(A):
 k,W=len(A),len(A[0])
 l,J,c,E=k,0,W,0
 for a in range(k):
  for C in range(W):
   if A[a][C]:l,J,c,E=min(l,a),max(J,a),min(c,C),max(E,C)
 return j([r[c:E+1]for r in A[l:J+1]],A[l][c],A[l+(J-l)//2][c+(E-c)//2])