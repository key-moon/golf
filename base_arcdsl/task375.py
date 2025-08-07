def P(A):return max(A for(B,A)in Z(A))
def J(A):return min(A for(B,A)in Z(A))
def V(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def Y(A,B):return E(A,(A[0]+42*B[0],A[1]+42*B[1]))
def M(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def L(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-J(A)+1
def X(j):return 0,j
def S(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def U(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=L(I);B=Y((0,0),(1,1));C=S(A);D=X(C);E=Y(D,(1,-1));F=U(B,E);G=M(I,0,F);return[*map(list,G)]