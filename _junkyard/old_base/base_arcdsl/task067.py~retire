def S(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def P(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(S(A,(0,B*C+C*E),(D,B))for C in range(n))
def Z(A):return next(iter(A))
def p(I):I=tuple(map(tuple,I));A=P(I,3);B=Z(A);return[*map(list,B)]