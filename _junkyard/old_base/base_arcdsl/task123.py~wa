def U(A):return max(A for(B,A)in Z(A))
def L(A):return min(A for(B,A)in Z(A))
def E(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-S(A)+1
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):return tuple(map(min,zip(*Z(A))))
def PZ(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def G(a,b):return a+b
def Q(a,b):return tuple(A+B for(A,B)in zip(a,b))
def Y(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def PE(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def R(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=X(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def W(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PX(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def PJ(A):return PP(A),PS(A)
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-L(A)+1
def H(A,a,b):return a if A else b
def K(a,b):return a,b
def M(x):return x>0
def J(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def V(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));B=PJ(I);E=PU(I,(0,0));F=P(I,0);L=J(B);N=M(F);O=H(N,L,B);A=PX(I,(0,0),O);C=PS(A);S=K(1,C);T=PX(A,(0,0),S);D=Y(T,C);U=R(D);X=Q(A,D);Z=Q(U,A);a=G(X,Z);b=W(a);c=V((1,1),10);d=PZ(E,c);e=PE(d,b);return[*map(list,e)]