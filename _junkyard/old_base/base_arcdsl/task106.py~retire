def P(a,b):return a+b
def Z(a,b):return tuple(A+B for(A,B)in zip(a,b))
def J(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def S(A):return tuple(tuple(A[::-1])for A in A[::-1])
def U(A):return tuple(A for A in zip(*A[::-1]))
def p(I):I=tuple(map(tuple,I));A=U(I);B=S(I);C=J(I);D=Z(I,A);E=Z(C,B);F=P(D,E);return[*map(list,F)]