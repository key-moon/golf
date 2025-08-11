def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return tuple(map(max,zip(*S(A))))
def ZP(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def V(A):return tuple(map(min,zip(*S(A))))
def PV(A):return PE(A),PL(A)
def Y(A):return max(A for(A,B)in S(A))
def L(A):return max(A for(B,A)in S(A))
def PG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return min(A for(B,A)in S(A))
def X(A):return min(A for(A,B)in S(A))
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-M(A)+1
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-X(A)+1
def PX(A):return X(A)+PE(A)//2,M(A)+PL(A)//2
def PP(A,B):return ZP(B,V(A),PV(A))
def PK(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=V(A)[1]+W(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PZ(A):
	if isinstance(A,tuple):return A[::-1]
	B=V(A)[0]+W(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def PM(A):return tuple(A for A in zip(*A[::-1]))
def PY(A):return next(iter(A))[0]
def R(A,B,C,D):
	M=U(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=J(A);V=E if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);Q|={(A,B)for(A,B)in V(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		N.add(frozenset(O))
	return frozenset(N)
def PQ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PH(A,a,b):return lambda x:A(a(x),b(x))
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PJ(A,B):return lambda x:A(x)==B
def PU(A,B):return lambda x:A(B(x))
def PW(A):return next(iter(A))
def PS(A,B):return next(A for A in A if B(A))
def K(a,b):return a==b
def Q(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def G(x):return x
def p(I):B=False;A=True;I=tuple(map(tuple,I));M=R(I,A,A,A);N=R(I,B,A,A);O=PW(N);P=PR(PP,I);E=PH(K,G,PM);S=PU(E,P);F=PS(M,S);J=PX(F);T=PP(O,I);C=PZ(T);U=R(C,B,A,A);V=PW(U);W=R(C,A,A,A);X=PR(PP,C);Y=PU(E,X);Z=PS(W,Y);a=PX(Z);b=Q(J,a);c=PQ(V,b);D=PK(I,c);d=R(D,B,A,A);e=PW(d);f=PP(e,D);L=H(f);g=R(L,B,A,A);h=PW(g);i=R(L,A,A,A);j=PY(F);k=PJ(PY,j);l=PS(i,k);m=PX(l);n=Q(J,m);o=PQ(h,n);p=PK(D,o);return[*map(list,p)]