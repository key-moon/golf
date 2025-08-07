def P(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def p(I):I=tuple(map(tuple,I));A=P(I,(0,0),(2,2));return[*map(list,A)]