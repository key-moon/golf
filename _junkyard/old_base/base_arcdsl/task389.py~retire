def S(A,a,b):return tuple(tuple(A if A!=a and A!=b else{a:b,b:a}[A]for A in A)for A in A)
def Z(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def P(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def U(A):return max(enumerate(A))[1]
def J(A):return next(iter(A))
def p(I):I=tuple(map(tuple,I));A=P(I);B=J(A);C=U(A);D=S(I,B,C);E=Z(D,5,0);return[*map(list,E)]