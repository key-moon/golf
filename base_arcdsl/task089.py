def ZJ(A,B):return type(B)(A(B)for B in B)
def PG(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Q(A):return tuple(map(max,zip(*S(A))))
def V(A):return max(A for(A,B)in S(A))
def Y(A):return max(A for(B,A)in S(A))
def PH(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def W(A):return min(A for(B,A)in S(A))
def L(A):return min(A for(A,B)in S(A))
def PQ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-W(A)+1
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PM(A):return L(A)+PX(A)//2,W(A)+PQ(A)//2
def ZZ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=M(A)[1]+Q(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PU(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
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
def PR(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def M(A):return tuple(map(min,zip(*S(A))))
def PL(A,B):return PG(ZJ(A,B))
def ZE(A,a,b):return lambda x:A(a(x),b(x))
def ZP(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PK(h,g,f):return lambda x:h(g(f(x)))
def PZ(A,B):return lambda x:A(B(x))
def PS(a,b):return a,b
def PW(A,B):return type(B)(B for B in B if B!=A)
def PY(A,B):return B.union(frozenset({A}))
def PP(A,B):return type(A)(A for A in A if B(A))
def K(A):return frozenset({A})
def PE(A,B):return max(A,key=B)
def ZU(A):return len(A)
def PJ(a,b):return type(a)((*a,*b))
def X(A,B):return A in B
def PV(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def G(x):return x
def p(I):I=tuple(map(tuple,I));Q=R(I,False,True,True);S=PS(10,10);A=PV(S);T=PS(2,A);U=PS(3,A);V=K(T);W=PY(U,V);B=PY(W,Q);C=ZP(X,2);D=ZP(X,3);Y=PZ(PV,M);Z=ZP(PZ,Y);a=ZP(ZS,PP);E=PZ(Z,a);F=ZS(PZ,PM);J=ZP(ZP,PR);b=E(C);c=E(D);d=ZE(PR,G,b);e=ZE(PR,G,c);f=PZ(C,PU);g=PZ(D,PU);L=PP(B,f);N=PE(L,ZU);h=PW(N,L);i=H(N);j=PK(F,J,d);k=j(i);l=PL(k,h);O=PP(B,g);P=PE(O,ZU);m=PW(P,O);n=PK(F,J,e);o=n(P);p=PL(o,m);q=PJ(l,p);r=ZZ(I,q);return[*map(list,r)]