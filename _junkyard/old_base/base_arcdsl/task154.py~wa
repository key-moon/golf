def M(A):return max(A for(A,B)in U(A))
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PL(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def G(A):return tuple(map(max,zip(*U(A))))
def ZV(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def ZP(A):return PW(A),PK(A)
def V(A):return max(A for(B,A)in U(A))
def Q(A):return min(A for(B,A)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def PK(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-Q(A)+1
def ZU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def ZL(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PH(A,B):return ZL(A,X(A),U(B))
def PG(A):return Y(A)+PW(A)//2,Q(A)+PK(A)//2
def PZ(A,B):return ZV(B,W(A),ZP(A))
def ZE(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PS(A):
	if isinstance(A,tuple):return A[::-1]
	B=W(A)[0]+G(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def PQ(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def ZZ(A):return tuple(A for A in zip(*A[::-1]))
def Z(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PL(A)-{X(A)})
def PP(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);T=E(A);U=L if C else S
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in U(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def ZJ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def H(A,B):return frozenset((A,B)for B in U(B))
def W(A):return tuple(map(min,zip(*U(A))))
def PJ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def K(A):return PW(A)>PK(A)
def PW(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-Y(A)+1
def ZX(A,B):return type(B)(A(B)for B in B)
def PE(A,B):return lambda x:A(x)==B
def PX(A,B):return lambda x:A(B(x))
def PY(A,a,b):return a if A else b
def ZS(A):return next(iter(A))
def PU(A,B):return next(A for A in A if B(A))
def PM(i):return i,0
def PV(A,B):return B(min(A,key=B,default=0))
def PR(A):return type(A)(B for A in A for B in A)
def ZY(b):return not b
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def ZM(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));M=Z(I);N=ZZ(I);O=P(M,2);Q=ZS(O);C=K(Q);A=PY(C,I,N);S=PP(A,True,False,True);B=P(S,5);T=ZX(PG,B);U=PV(T,ZS);V=PX(ZS,PG);D=PE(V,U);X=PX(ZY,D);E=PU(B,D);F=PU(B,X);Y=W(E);a=W(F);b=PZ(E,A);c=PZ(F,A);d=PS(b);e=PS(c);f=PJ(d,5);G=H(5,f);g=PJ(e,5);J=H(5,g);h=PW(G);i=PW(J);j=ZM(3,h);k=ZM(3,i);l=PM(j);m=PM(k);n=ZM(Y,l);o=R(a,m);p=ZJ(G,n);q=ZJ(J,o);r=PR(B);s=PH(A,r);t=ZE(s,p);L=ZE(t,q);u=PQ(L);v=PY(C,L,u);return[*map(list,v)]