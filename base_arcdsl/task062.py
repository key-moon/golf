def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Q(A):return tuple(map(max,zip(*S(A))))
def ZU(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def ZP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Y(A):return max(A for(A,B)in S(A))
def L(A):return max(A for(B,A)in S(A))
def M(A):return min(A for(B,A)in S(A))
def X(A):return min(A for(A,B)in S(A))
def PQ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-M(A)+1
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-X(A)+1
def PW(A):return X(A)+PM(A)//2,M(A)+PQ(A)//2
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(a,b):
	A,B=PW(S(a));C,D=PW(S(b))
	if A==C:return 0,1 if B<D else-1
	elif B==D:return 1 if A<C else-1,0
	elif A<C:return 1,1 if B<D else-1
	elif A>C:return-1,1 if B<D else-1
def PX(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PZ(A,B):return ZU(B,V(A),PG(A))
def ZZ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=V(A)[1]+Q(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PS(A):
	if isinstance(A,tuple):return A[::-1]
	B=V(A)[0]+Q(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def G(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PR(A):return PQ(A)==len(A)and PM(A)==1
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
def PH(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def V(A):return tuple(map(min,zip(*S(A))))
def PG(A):return PM(A),PQ(A)
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PJ(A,B):return lambda x:A(x)==B
def PU(A,B):return lambda x:A(B(x))
def PL(A,a,b):return a if A else b
def PE(a,b):return a,b
def ZE(A):return max(enumerate(A))[1]
def PK(A):return next(iter(A))
def PP(A,B):return type(A)(A for A in A if B(A))
def PY(A,B):return min(A,key=B)
def PV(A,B):return max(A,key=B)
def ZS(A):return len(A)
def ZJ(b):return not b
def W(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def ZX(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));L=U(I);C=R(I,True,False,True);D=PX(I,L,3);A=PV(C,ZS);E=PY(C,ZS);F=K(A,E);M=PK(F);N=ZE(F);J=PZ(A,D);B=PR(E);O=PS(J);P=H(J);Q=PL(B,O,P);S=PL(B,M,0);T=PL(B,0,N);X=G(Q);Y=PJ(PK,3);Z=PU(ZJ,Y);a=PP(X,Z);b=V(A);c=PG(A);d=PE(S,T);e=W(c,d);f=ZX(b,e);g=PH(a,f);h=ZZ(D,g);return[*map(list,h)]