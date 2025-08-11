def Q(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def L(A):return max(A for(A,B)in J(A))
def E(A):return min(A for(A,B)in J(A))
def X(A):return max(A for(B,A)in J(A))
def V(A):return min(A for(B,A)in J(A))
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return X(A)-V(A)+1
def G(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-E(A)+1
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PJ(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def Y(A):return tuple(map(min,zip(*J(A))))
def H(A):return G(A),K(A)
def PS(A):return tuple(A[1:-1]for A in A[1:-1])
def W(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def M(A,B):return PJ(B,Y(A),H(A))
def R(A):return next(iter(A))[0]
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in Q(A)-{U(A)})
def S(A,n):return frozenset(A for A in A if len(A)==n)
def PP(A):return next(iter(A))
def Z(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));A=P(I);B=S(A,4);C=PP(B);D=Z(A,B);E=PP(D);F=R(C);G=R(E);H=M(C,I);J=PS(H);K=W(J,G,F);return[*map(list,K)]