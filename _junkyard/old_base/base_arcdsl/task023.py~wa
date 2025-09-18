def PL(A,B):return type(B)(A(B)for B in B)
def PS(A):return type(A)(B for A in A for B in A)
def Y(A):return tuple(map(max,zip(*Z(A))))
def X(A):return tuple(map(min,zip(*Z(A))))
def E(A):return max(A for(A,B)in Z(A))
def U(A):return max(A for(B,A)in Z(A))
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-L(A)+1
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-J(A)+1
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return min(A for(B,A)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def S(A):
	if len(A)==0:return A
	return PU(A,(-J(A),-L(A)))
def PJ(A):return R(A),PZ(A)
def P(A,B):
	C=set();K=S(B);D,E=len(A),len(A[0]);L,M=PJ(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in PU(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def PP(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def Q(a,b):return a+b
def PY(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def K(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=X(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def M(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=X(A)[1]+Y(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def W(A):
	if isinstance(A,tuple):return A[::-1]
	B=X(A)[0]+Y(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def V(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PU(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def H(A,B):return PS(PL(A,B))
def PX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def G(a,b):return a,b
def p(I):I=tuple(map(tuple,I));U=PP(5,(2,2));B=V(U);X=P(I,B);Y=PX(PU,B);Z=H(Y,X);C=PY(I,8,Z);a=PP(5,(1,1));b=G(2,1);c=PP(8,b);A=Q(c,a);D=V(A);d=P(C,D);e=PX(PU,D);f=H(e,d);E=PY(C,2,f);g=G(1,3);h=PP(5,g);F=V(h);i=P(E,F);j=PX(PU,F);k=H(j,i);J=PY(E,2,k);l=W(A);L=V(l);m=P(J,L);n=PX(PU,L);o=H(n,m);N=PY(J,2,o);O=K(A);R=V(O);p=P(N,R);q=PX(PU,R);r=H(q,p);S=PY(N,2,r);s=M(O);T=V(s);t=P(S,T);u=PX(PU,T);v=H(u,t);w=PY(S,2,v);return[*map(list,w)]