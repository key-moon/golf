def V(A):return max(A for(A,B)in H(A))
def J(A):return min(A for(A,B)in H(A))
def GG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def H(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return max(A for(B,A)in H(A))
def E(A):return min(A for(B,A)in H(A))
def M(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def R(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def W(A):return tuple(A for A in zip(*A[::-1]))
def L(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-E(A)+1
def S(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-J(A)+1
def Z(A,B):return type(B)(A(B)for B in B)
def U(A,B):return lambda x:A(B(x))
def Q(A,a,b):return a if A else b
def G(A):return max(set(A),key=A.count)
def GH(A):return len(A)
def X(a,b):return a>b
def K(A,B):return tuple(A for B in range(B))
def P(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def p(I):I=tuple(map(tuple,I));E=W(I);B=Z(G,I);C=Z(G,E);F=K(B,1);H=K(C,1);D=U(GH,P);J=D(B);N=D(C);A=X(N,J);O=Q(A,S,L);T=O(I);V=W(F);Y=Q(A,H,V);a=Q(A,M,R);b=a(Y,T);return[*map(list,b)]