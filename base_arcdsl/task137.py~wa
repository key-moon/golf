def H(A):return type(A)(B for A in A for B in A)
def U(A):return max(A for(A,B)in Z(A))
def J(A):return max(A for(B,A)in Z(A))
def X(A):return min(A for(B,A)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-X(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-S(A)+1
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return tuple(map(max,zip(*Z(A))))
def PX(A):
	if len(A)==0:return A
	G,H=E(A);I,J=V(A);B,C=min(G,I),min(H,J);D,F=max(G,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,F)for A in range(B,D+1)};L={(B,A)for A in range(C,F+1)}|{(D,A)for A in range(C,F+1)};return frozenset(K|L)
def K(A):return S(A)+Q(A)//2,X(A)+R(A)//2
def PU(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PP(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def E(A):return tuple(map(min,zip(*Z(A))))
def W(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def G(A,B):return H(PJ(A,B))
def PJ(A,B):return type(B)(A(B)for B in B)
def PS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PE(a,b):return tuple(zip(a,b))
def Y(A,B,C):return tuple(range(A,B,C))
def L(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def M(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));A=P(I);B=W(I,A);C=K(B);F=E(B);H=M(C,F);J=L(-1,9);N=Y(0,9,1);O=Y(0,J,-1);D=PS(L,H);Q=PJ(D,N);R=PJ(D,O);S=PE(Q,R);T=G(PX,S);U=PP(T,C);V=PU(I,A,U);return[*map(list,V)]