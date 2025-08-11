def W(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def H(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def U(A,B,C):
	H,I=len(A),len(A[0]);K=J(A);D=list(list(A)for A in A)
	for(F,G)in E(C):
		if 0<=F<H and 0<=G<I:
			if D[F][G]==K:D[F][G]=B
	return tuple(tuple(A)for A in D)
def G(A):return tuple(A for A in zip(*A[::-1]))
def X(A):return Z(A)|S(A)
def R(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def V(A,B):return W(K(A,B))
def K(A,B):return type(B)(A(B)for B in B)
def Q(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def L(A,B):return lambda x:A(B(x))
def M(A,B):return max(A,key=B)
def PP(A):return len(A)
def P(a,b):return a&b
def p(I):I=tuple(map(tuple,I));A=G(I);B=Y(I,1);C=Y(A,1);D=X((0,0));E=V(X,D);F=Q(R,C);H=K(F,E);J=Q(P,B);N=L(PP,J);O=M(H,N);S=U(I,2,O);return[*map(list,S)]