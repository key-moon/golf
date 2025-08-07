def S(A):return tuple(map(min,zip(*Z(A))))
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def J(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def M(A,B):return J(A,(A[0]+42*B[0],A[1]+42*B[1]))
def W(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def X(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def G(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def U(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=S(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def L(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def V(A,B):return type(B)(A(B)for B in B)
def Y(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def Q(a,b):return tuple(zip(a,b))
def E(A):return max(A,default=0)
def p(I):I=tuple(map(tuple,I));C=U(I);D=L(Q,I,C);F=Y(V,E);A=V(F,D);H=P(A);B=X(A,0,H);J=W(B,(0,0));K=M((0,0),(1,1));N=G(B,J,K);return[*map(list,N)]