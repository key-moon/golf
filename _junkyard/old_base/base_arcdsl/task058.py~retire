def U(A):return max(A for(A,B)in P(A))
def Z(A):return min(A for(A,B)in P(A))
def J(A):return max(A for(B,A)in P(A))
def X(A):return min(A for(B,A)in P(A))
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PX(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def E(A):return tuple(map(min,zip(*P(A))))
def PZ(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def G(a,b):return a+b
def W(a,b):return tuple(A+B for(A,B)in zip(a,b))
def R(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for J in A:
			D=tuple()
			for F in J:D=D+tuple(F for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		G,H=E(A);K,L=-G,-H;M=PX(A,(K,L));I=set()
		for(F,(N,O))in M:
			for P in range(B):
				for Q in range(B):I.add((F,(N*B+P,O*B+Q)))
		return PX(frozenset(I),(G,H))
def L(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def V(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def PQ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PE(A):return tuple(A for A in zip(*A[::-1]))
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-X(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-Z(A)+1
def PW(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,n):
	if n==1:return A
	return Q(A,PM(A,n-1))
def PY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PU(h,g,f):return lambda x:h(g(f(x)))
def Q(A,B):return lambda x:A(B(x))
def H(A,a,b):return a if A else b
def K(a,b):return a,b
def PS(A,B):return B.union(frozenset({A}))
def S(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def M(A):return frozenset({A})
def PG(n):return n%2==0
def Y(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));B=PJ(I);D=K(1,2);E=K(2,2);F=K(2,1);J=K(3,1);A=PZ(3,(1,1));N=R(A,4);O=M((1,0));C=PS((1,1),O);P=PS(D,C);T=PS(E,P);U=PQ(N,0,T);X=L(A,5);Z=V(X,3);a=PS(F,C);b=PS(J,a);c=PQ(Z,0,b);d=PG(B);e=H(d,U,c);f=PZ(0,(1,1));g=PY(V,f);h=PU(g,S,PP);i=PV(W,A);j=Q(i,h);k=PY(V,A);l=Q(k,PP);m=PW(G,j,PE);n=PW(G,l,m);o=Y(B,4);p=PM(n,o);q=p(e);return[*map(list,q)]