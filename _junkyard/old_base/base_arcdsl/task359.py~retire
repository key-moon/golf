def U(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def H(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def J(A):return max(A for(B,A)in Z(A))
def E(A):return min(A for(B,A)in Z(A))
def X(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def L(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def R(A):return tuple(A for A in zip(*A[::-1]))
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-E(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-S(A)+1
def PP(A,B):return type(B)(A(B)for B in B)
def V(A,B):return lambda x:A(B(x))
def W(A,a,b):return a if A else b
def P(A):return max(set(A),key=A.count)
def PZ(A):return len(A)
def Y(a,b):return a>b
def G(A,B):return tuple(A for B in range(B))
def M(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def p(I):I=tuple(map(tuple,I));E=R(I);B=PP(P,I);C=PP(P,E);F=G(B,1);H=G(C,1);D=V(PZ,M);J=D(B);N=D(C);A=Y(N,J);O=W(A,Q,K);S=O(I);T=R(F);U=W(A,H,T);Z=W(A,X,L);a=Z(U,S);return[*map(list,a)]