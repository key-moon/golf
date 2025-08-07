def P(A):return tuple(tuple(A[::-1])for A in A[::-1])
def p(I):I=tuple(map(tuple,I));A=P(I);return[*map(list,A)]