def PH(A,B):return type(B)(A(B)for B in B)
def PX(A):return type(A)(B for A in A for B in A)
def PG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def PZ(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def L(A):return max(A for(A,B)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def E(A):return max(A for(B,A)in Z(A))
def V(A):return min(A for(B,A)in Z(A))
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-V(A)+1
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-J(A)+1
def ZU(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PV(A):return PJ(A),PE(A)
def X(A):C,D=len(A),len(A[0]);B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);E=tuple(A for(A,B)in enumerate(PP(A))if len(set(B))==1);F=frozenset({frozenset({(A[B][C],(B,C))for C in range(D)})for B in B});G=frozenset({frozenset({(A[C][B],(C,B))for C in range(C)})for B in E});return F|G
def U(A):return frozenset((B,A[1])for B in range(30))
def G(A,B):return ZU(B,Y(A),PV(A))
def ZS(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PP(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Y(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PM(A):return tuple(A for A in zip(*A[::-1]))
def PL(A):return next(iter(A))[0]
def PW(A):return PE(A)==len(A)and PJ(A)==1
def S(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PZ(A))
def PQ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return tuple(map(min,zip(*Z(A))))
def K(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PU(A,B):return PX(PH(A,B))
def ZZ(A,a,b):return lambda x:A(a(x),b(x))
def PK(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def R(A,B):return lambda x:A(x)==B
def PY(h,g,f):return lambda x:h(g(f(x)))
def H(A,B):return lambda x:A(B(x))
def PS(A,a,b):return a if A else b
def Q(A,B):return type(A)(A for A in A if B(A))
def M(x):return x>0
def ZP(A):return len(A)
def P(a,b):return a&b
def ZJ(b):return not b
def W(x):return x
def p(I):I=tuple(map(tuple,I));h=PM(I);C=X(I);D=Q(C,PW);E=ZP(D);F=M(E);B=PS(F,W,PP);A=B(I);J=PR(G,A);L=R(PL,0);N=H(ZJ,L);O=S(A);T=Q(O,N);V=PR(K,0);a=PK(PU,U);b=PY(a,V,J);c=ZZ(PQ,b,Y);d=ZZ(P,Z,c);e=PU(d,T);f=ZS(A,0,e);g=B(f);return[*map(list,g)]