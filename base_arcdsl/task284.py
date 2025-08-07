def V(A):return max(A for(A,B)in J(A))
def Y(A):return max(A for(B,A)in J(A))
def W(A):return min(A for(B,A)in J(A))
def PW(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-W(A)+1
def PV(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def ZZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PK(A,B):return ZJ(A,E(A),J(B))
def PJ(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def ZS(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def ZJ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PL(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=M(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PP(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in J(A)if 0<=A<D and 0<=C<E)
def PG(A):return next(iter(A))[0]
def P(A):return tuple(map(lambda x:sum(x)//len(A),zip(*J(A))))
def L(A):return min(A for(A,B)in J(A))
def PS(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();P,Q=len(A),len(A[0]);R=U(A);S=X if C else Z
	for F in R:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in S(G)if 0<=A<P and 0<=B<Q}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def PH(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return tuple(map(max,zip(*J(A))))
def H(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*J(A)))))
def K(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*J(A)))))
def M(A):return tuple(map(min,zip(*J(A))))
def G(A):return PV(A)>PW(A)
def PU(A,B):return lambda x:A(B(x))
def PY(A,a,b):return a if A else b
def PE(a,b):return a,b
def PM(A,B):return B.union(frozenset({A}))
def ZU(A):return max(enumerate(A))[1]
def PR(A):return next(iter(A))
def PZ(A):return frozenset({A})
def PQ(A):return type(A)(B for A in A for B in A)
def ZP(A,B):return tuple(sorted(A,key=B))
def PX(a,b):return type(a)((*a,*b))
def ZE(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def R(x):return x
def p(I):a=False;B=True;I=tuple(map(tuple,I));b=PS(I,B,a,B);c=PQ(b);d=G(c);D=PY(d,R,PL);E=D(I);e=PS(E,B,a,B);F=ZP(e,L);N=PR(F);O=ZU(F);S=PG(N);T=PG(O);U=PU(PR,J);V=U(N);f=U(O);W=PJ(V,f);C=P(W);g=PJ(V,C);h=ZJ(E,T,W);X=ZJ(h,S,g);i=ZE(C,(1,0));j=PZ(C);Y=PM(i,j);Z=PP(Y,X);k=PE(0,-2);l=PH(Z,(0,2));m=PH(Z,k);A=PX(l,m);n=M(A);o=K(A);p=PJ(n,o);q=PH(p,(-1,0));r=H(A);s=Q(A);t=PJ(r,s);u=PH(t,(1,0));v=ZS(X,A);w=ZJ(v,S,q);x=ZJ(w,T,u);y=PK(x,Y);z=D(y);return[*map(list,z)]