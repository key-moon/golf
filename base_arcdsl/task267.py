def Z(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def p(I):I=tuple(map(tuple,I));A=P(I);B=Z(I,A,0);C=P(B);D=Z(B,C,A);return[*map(list,D)]