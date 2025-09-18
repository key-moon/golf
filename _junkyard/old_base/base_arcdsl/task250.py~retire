def G(A):return type(A)(B for A in A for B in A)
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def R(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def J(A):return max(A for(B,A)in P(A))
def X(A):return min(A for(B,A)in P(A))
def E(A):return max(A for(A,B)in P(A))
def S(A):return min(A for(A,B)in P(A))
def W(A):G,H=S(A)-1,X(A)-1;I,K=E(A)+1,J(A)+1;B,C=min(G,I),min(H,K);D,F=max(G,I),max(H,K);L={(A,C)for A in range(B,D+1)}|{(A,F)for A in range(B,D+1)};M={(B,A)for A in range(C,F+1)}|{(D,A)for A in range(C,F+1)};return frozenset(L|M)
def K(A,B):return PZ(A,Z(A),P(B))
def PZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def U(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in P(a)for(C,D)in P(b))
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Q(A,B):return G(PP(A,B))
def PP(A,B):return type(B)(A(B)for B in B)
def H(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def V(A,B):return lambda x:A(B(x))
def L(A):return frozenset({A})
def M(A,B):return min(A,key=B)
def p(I):I=tuple(map(tuple,I));B=Y(I,2);C=W(B);D=PP(L,C);A=Y(I,5);E=H(M,D);F=H(H,U);G=V(F,L);J=V(E,G);N=Q(J,A);O=K(I,A);P=PZ(O,5,N);return[*map(list,P)]