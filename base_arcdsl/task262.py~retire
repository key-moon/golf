def M(A,B):return type(B)(A(B)for B in B)
def X(A):return type(A)(B for A in A for B in A)
def V(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return frozenset((A[0],B)for B in range(30))
def W(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def S(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def E(A,B):return X(M(A,B))
def L(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def J(A,B):return lambda x:A(x)==B
def Y(h,g,f):return lambda x:h(g(f(x)))
def Q(A):return max(enumerate(A))[1]
def U(A,B):return type(A)(A for A in A if B(A))
def p(I):I=tuple(map(tuple,I));B=S(I,5);C=L(J,Q);D=L(U,B);F=L(E,Z);A=Y(F,D,C);G=A(0);H=A(2);K=A(1);M=W(I,2,G);N=W(M,3,H);O=W(N,4,K);return[*map(list,O)]