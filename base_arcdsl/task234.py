def PV(A,B):return type(B)(B for B in B if B!=A)
def PK(A):return next(iter(A))
def PU(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def R(A):return tuple(map(max,zip(*J(A))))
def W(A):return tuple(map(min,zip(*J(A))))
def V(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def PY(A):return L(A)+PL(A)//2,Q(A)+PM(A)//2
def H(a,b):return V(a,b)==1
def U(a,b):return len(set(A for(B,A)in J(a))&set(A for(B,A)in J(b)))>0
def PH(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return max(A for(B,A)in J(A))
def Q(A):return min(A for(B,A)in J(A))
def M(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def PX(A):F,G=L(A)-1,Q(A)-1;H,I=M(A)+1,Y(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def X(A,B):
	I,J=PY(A);K,L=PY(B);C,D=0,0
	if U(A,B):C=1 if I<K else-1
	else:D=1 if J<L else-1
	E,F=C,D;G=0
	while not H(A,B)and G<42:G+=1;E+=C;F+=D;A=PR(A,(C,D))
	return E-C,F-D
def G(A):
	if len(A)==0:return frozenset({})
	B=J(A);C,D=W(B);E,F=R(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def PG(A,B):return ZU(A,E(A),J(B))
def ZU(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PZ(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in J(A)if 0<=A<D and 0<=C<E)
def PW(A):return next(iter(A))[0]
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PU(A)-{E(A)})
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def PR(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Z(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-Q(A)+1
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-L(A)+1
def ZJ(A,a,b):return lambda x:A(a(x),b(x))
def ZZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PQ(h,g,f):return lambda x:h(g(f(x)))
def ZP(A,B):return PK(PV(B,A))
def ZE(A):return max(enumerate(A))[1]
def PE(A,B):return next(A for A in A if B(A))
def PS(A,B):return type(A)(A for A in A if B(A))
def ZS(A):return len(A)
def PJ(a,b):return a>b
def PP(a,b):return a==b
def K(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));B=P(I);F=ZJ(K,PL,PM);H=ZJ(PP,ZS,F);C=PE(B,H);A=ZP(B,C);D=PW(A);J=ZZ(PJ,3);L=ZZ(PZ,I);M=ZZ(Z,D);N=PQ(L,S,ZE);O=PQ(J,M,N);Q=PS(A,O);R=PX(Q);E=G(R);T=PG(I,A);U=X(E,C);V=PR(E,U);W=ZU(T,D,V);return[*map(list,W)]