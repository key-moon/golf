def PH(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def M(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def L(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PV(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def G(A):return max(A for(A,B)in E(A))
def W(A):return min(A for(A,B)in E(A))
def ZU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return max(A for(B,A)in E(A))
def R(A):return min(A for(B,A)in E(A))
def PR(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Q(A)-R(A)+1
def PG(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return G(A)-W(A)+1
def ZZ(A):return PG(A),PR(A)
def P(A,B):
	C=set();K=X(B);D,E=len(A),len(A[0]);L,M=ZZ(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in ZJ(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def PQ(A):F,H=W(A)-1,R(A)-1;I,J=G(A)+1,Q(A)+1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def PY(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=K(A);J,L=-F,-G;M=ZJ(A,(J,L));H=set()
		for(E,(N,O))in M:
			for P in range(B):
				for Q in range(B):H.add((E,(N*B+P,O*B+Q)))
		return ZJ(frozenset(H),(F,G))
def ZX(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def Y(A):return len(PV(A))
def PJ(A,B,C,D):
	K=V(A)if D else None;N=set();G=set();Q,R=len(A),len(A[0]);T=L(A);U=M if C else S
	for E in T:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		O={(H,E)};I={E}
		while len(I)>0:
			P=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:O.add((J,F));G.add(F);P|={(A,B)for(A,B)in U(F)if 0<=A<Q and 0<=B<R}
			I=P-G
		N.add(frozenset(O))
	return frozenset(N)
def X(A):
	if len(A)==0:return A
	return ZJ(A,(-W(A),-R(A)))
def ZJ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PS(A,B):return frozenset((A,B)for B in E(B))
def K(A):return tuple(map(min,zip(*E(A))))
def V(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PK(A,B):return PH(ZY(A,B))
def PM(A,B):return type(A)(A(B)for A in A)
def ZY(A,B):return type(B)(A(B)for B in B)
def ZV(A,a,b):return lambda x:A(a(x),b(x))
def ZE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZL(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PE(A,B):return lambda x:A(x)==B
def ZP(h,g,f):return lambda x:h(g(f(x)))
def PX(A,B):return lambda x:A(B(x))
def H(A,B,C):return tuple(range(A,B,C))
def ZS(A):return next(iter(A))
def PU(A,B):return type(A)(A for A in A if B(A))
def U(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PW(A,B):return max(A,key=B)
def Z(a,b):return type(a)(A for A in a if A not in b)
def PL(a,b):return type(a)((*a,*b))
def PP(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def PZ(x):return x
def p(I):I=tuple(map(tuple,I));B=PJ(I,False,True,True);C=PW(B,Y);D=X(C);E=ZE(PE,ZS);F=PX(E,V);G=ZV(PU,PZ,F);A=ZV(Z,PZ,G);J=ZE(ZL,PY);L=H(1,4,1);M=ZY(J,L);N=ZE(PS,0);O=PX(N,PQ);Q=ZV(PL,PZ,O);R=ZE(P,I);S=ZE(ZL,PP);T=ZE(ZY,U);W=ZE(ZE,ZJ);a=ZP(S,K,A);b=ZP(R,Q,A);c=ZV(ZY,a,b);d=PX(T,c);e=ZV(PK,W,d);f=PM(M,D);g=PK(e,f);h=ZX(I,g);return[*map(list,h)]