def p(A):
 B={}
 for C in sum(A,[]):B[C]=B.get(C,0)+1
 D=sorted(B.items(),key=lambda C:(-C[1],C[0]));return[[B if C>A else 0 for(B,C)in D]for A in range(D[0][1])]