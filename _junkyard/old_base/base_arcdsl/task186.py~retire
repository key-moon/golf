def V(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
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
def E(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def W(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def U(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def L(A,a,b):return a if A else b
def Y(A,B):return B.union(frozenset({A}))
def X(j):return 0,j
def Z(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def M(A):return len(A)
def S(a,b):return a==b
def p(I):I=tuple(map(tuple,I));C=U(I,1);A=M(C);D=Z(A);F=E(0,(3,3));G=X(D);B=J((0,0),G);H=S(A,4);K=Y((1,1),B);N=L(H,K,B);O=W(F,2,N);return[*map(list,O)]