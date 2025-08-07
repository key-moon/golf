def R(A,B):return type(B)(A(B)for B in B)
def M(A):return type(A)(B for A in A for B in A)
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PZ(A):return tuple(A[1:-1]for A in A[1:-1])
def X(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def K(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PS(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def S(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def Q(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def L(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def V(A,B):return M(R(A,B))
def PP(A,a,b):return lambda x:A(a(x),b(x))
def H(A,n):
	if n==1:return A
	return Y(A,H(A,n-1))
def Y(A,B):return lambda x:A(B(x))
def E(a,b):return frozenset((B,A)for A in b for B in a)
def PJ(A):return max(enumerate(A))[1]
def W(A):return next(iter(A))
def U(A,B):return type(A)(A for A in A if B(A))
def P(a,b):return a&b
def J(a,b):return a==b
def p(I):I=tuple(map(tuple,I));A=L(I,2);B=L(I,0);C=E(A,A);D=H(W,2);F=Y(W,PJ);G=PP(J,D,F);M=U(C,G);N=PP(X,W,PJ);O=V(N,M);R=P(O,B);T=PS(I,9,R);Z=PZ(T);a=S(Z);b=Q(a,(1,1));c=K(I,b);return[*map(list,c)]