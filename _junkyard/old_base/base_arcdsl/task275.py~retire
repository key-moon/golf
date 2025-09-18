def J(A):return max(A for(B,A)in P(A))
def X(A):return min(A for(B,A)in P(A))
def U(A):return max(A for(A,B)in P(A))
def S(A):return min(A for(A,B)in P(A))
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-S(A)+1
def W(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PX(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PE(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def E(A):return tuple(map(min,zip(*P(A))))
def PV(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def K(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(PV(A,(B*C+C*E,0),(B,D))for C in range(n))
def PZ(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(PV(A,(0,B*C+C*E),(D,B))for C in range(n))
def V(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for J in A:
			D=tuple()
			for F in J:D=D+tuple(F for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		G,H=E(A);K,L=-G,-H;M=PE(A,(K,L));I=set()
		for(F,(N,O))in M:
			for P in range(B):
				for Q in range(B):I.add((F,(N*B+P,O*B+Q)))
		return PE(frozenset(I),(G,H))
def PY(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=E(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def Z(A):return len(W(A))
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def L(A):return H(A)>PS(A)
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-X(A)+1
def PL(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PU(h,g,f):return lambda x:h(g(f(x)))
def Q(A,a,b):return a if A else b
def G(A,B):return min(A,key=B)
def R(A,B):return max(A,key=B)
def PJ(A):return type(A)(B for A in A for B in A)
def PP(A,B):return tuple(A for B in range(B))
def p(I):I=tuple(map(tuple,I));E=L(I);F=Q(E,K,PZ);A=F(I,2);H=G(A,Z);B=R(A,Z);C=PS(B);J=PL(PP,C);D=PU(M,PJ,J);N=V(B,C);O=D(H);P=D(O);S=Y(P,0);T=PY(N,0,S);return[*map(list,T)]