def PK(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def ZS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PG(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-Y(A)+1
def PZ(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def ZU(A,B):return PZ(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PQ(A):return Y(A)+PY(A)//2,G(A)+PG(A)//2
def W(A,B,C):
	G,H=len(A),len(A[0]);I=X(A);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def ZV(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def ZE(A):return PY(A)==len(A)and PG(A)==1
def M(A):return max(A for(B,A)in U(A))
def G(A):return min(A for(B,A)in U(A))
def Q(A):return max(A for(A,B)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def H(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=L if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def ZZ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PH(A):return PY(A),PG(A)
def PV(A,B):return PK(ZL(A,B))
def ZL(A,B):return type(B)(A(B)for B in B)
def ZY(A,a,b):return lambda x:A(a(x),b(x))
def ZJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PS(A,B):return lambda x:A(x)==B
def PR(h,g,f):return lambda x:h(g(f(x)))
def PJ(A,B):return lambda x:A(B(x))
def PU(a,b):return a,b
def K(A,B,C):return tuple(range(A,B,C))
def ZP(A):return next(iter(A))
def PP(A,B):return type(A)(A for A in A if B(A))
def PM(j):return 0,j
def PL(i):return i,0
def V(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def J(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PX(Aa):return min(Aa,default=0)
def P(a,b):return type(a)(A for A in a if A not in b)
def PE(a,b):return type(a)((*a,*b))
def R(a,b):return a==b
def PW(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def ZM(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):N=False;I=tuple(map(tuple,I));B=H(I,N,N,True);O=PS(ZP,2);A=ZX(PP,O);S=PJ(Q,A);T=PJ(M,A);U=PJ(Y,A);X=PJ(G,A);Z=ZY(R,S,Q);a=ZY(R,T,M);b=ZY(R,U,Y);c=ZY(R,X,G);d=PJ(PW,b);e=PJ(PW,c);f=ZY(ZM,d,Z);g=ZY(ZM,e,a);h=ZY(PU,f,g);i=PJ(PQ,A);C=ZY(ZU,i,h);j=PV(C,B);k=ZV(I,2,j);l=PJ(ZE,C);D=PP(B,l);m=P(B,D);E=PR(V,PX,PH);n=PJ(J,E);o=PJ(PW,E);p=ZX(K,1);F=ZY(p,o,n);q=ZJ(ZL,PL);r=ZJ(ZL,PM);s=ZJ(ZJ,ZZ);L=PJ(s,C);t=PJ(q,F);u=PJ(r,F);v=ZY(PV,L,t);w=ZY(PV,L,u);x=PV(v,m);y=PV(w,D);z=PE(x,y);A0=W(k,3,z);return[*map(list,A0)]