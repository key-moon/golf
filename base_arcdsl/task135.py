def Z(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def P(j):return 0,j
def p(I):I=tuple(map(tuple,I));A=P(6);B=Z(I,A,(3,3));return[*map(list,B)]