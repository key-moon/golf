def W(A):return max(A for(A,B)in U(A))
def M(A):return max(A for(B,A)in U(A))
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def PP(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return min(A for(B,A)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def E(A):
	if len(A)==0:return A
	return PY(A,(-Y(A),-Q(A)))
def PZ(A):
	B=E(A);D=PJ(B)
	for C in range(1,D):
		F=PY(B,(-C,0));G=frozenset({(B,(A,C))for(B,(A,C))in F if A>=0})
		if G.issubset(B):return C
def R(A):
	B=E(A);C=PX(B)
	for D in range(1,C):
		F=PY(B,(0,-D));G=frozenset({(B,(C,A))for(B,(C,A))in F if A>=0})
		if G.issubset(B):return D
	return C
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def K(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def X(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PP(A))
def L(A):return S(A)|J(A)
def PY(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PG(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-Q(A)+1
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-Y(A)+1
def PU(A,B):return PL(PQ(A,B))
def PQ(A,B):return type(B)(A(B)for B in B)
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def H(a,b):return a,b
def PE(j):return 0,j
def PS(i):return i,0
def V(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def PL(A):return type(A)(B for A in A for B in A)
def Z(a,b):return type(a)(A for A in a if A not in b)
def G(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));A=PJ(I);B=PX(I);C=X(I);D=P(C,0);E=Z(C,D);F=PL(E);J=H(A,1);M=H(1,B);N=V(A);O=V(B);Q=PS(O);S=PE(N);T=PG(I,Q,M);U=PG(I,S,J);W=K(U);Y=K(T);a=PZ(W);b=R(Y);c=H(a,b);d=PM(G,c);e=L((0,0));f=PU(L,e);g=PQ(d,f);h=PM(PY,F);i=PU(h,g);j=PW(I,i);return[*map(list,j)]