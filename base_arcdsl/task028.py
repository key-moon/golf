def Q(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):return tuple(map(max,zip(*S(A))))
def E(A):return tuple(map(min,zip(*S(A))))
def K(A):
	if len(A)==0:return A
	G,H=E(A);I,J=X(A);B,C=min(G,I),min(H,J);D,F=max(G,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,F)for A in range(B,D+1)};L={(B,A)for A in range(C,F+1)}|{(D,A)for A in range(C,F+1)};return frozenset(K|L)
def U(A):return frozenset((A[0],B)for B in range(30))
def P(A):return A[len(A)//2+len(A)%2:]
def Y(A):return A[:len(A)//2]
def W(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def V(a,b):return a+b
def G(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A):
	if isinstance(A,tuple):return A[::-1]
	B=E(A)[0]+X(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def L(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));D=J(I);A=Y(I);E=P(I);B=Z(A);F=Z(E);H=U((2,0));N=K(D);O=L(H,N);C=G(A,B,O);Q=M(C);R=W(Q,B,F);S=V(C,R);return[*map(list,S)]