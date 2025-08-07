def P(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def p(I):I=tuple(map(tuple,I));A=P(I,7,5);return[*map(list,A)]