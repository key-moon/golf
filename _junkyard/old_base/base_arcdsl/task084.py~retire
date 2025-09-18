def S(A):return max(A for(A,B)in P(A))
def Z(A):return min(A for(A,B)in P(A))
def Y(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def L(A,B):return U(A,(A[0]+42*B[0],A[1]+42*B[1]))
def V(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def X(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return S(A)-Z(A)+1
def E(a,b):return a,b
def J(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def p(I):I=tuple(map(tuple,I));B=X(I);A=J(B);C=J(A);D=E(C,1);F=E(A,1);G=L(D,(-1,1));H=L(F,(0,1));K=V(I,2,G);M=V(K,4,H);return[*map(list,M)]