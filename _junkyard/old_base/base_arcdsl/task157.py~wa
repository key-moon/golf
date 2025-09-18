def PK(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def H(A):return tuple(map(max,zip(*U(A))))
def Q(A):return tuple(map(min,zip(*U(A))))
def K(A):
	if len(A)==0:return frozenset({})
	B=U(A);C,D=Q(B);E,F=H(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def M(A):return max(A for(B,A)in U(A))
def G(A):return min(A for(B,A)in U(A))
def W(A):return max(A for(A,B)in U(A))
def PX(A):F,H=V(A)-1,G(A)-1;I,J=W(A)+1,M(A)+1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def PR(B):
	if len(B)==0:return frozenset({})
	return K(B)-U(B)
def PQ(A,B):return ZU(A,L(A),U(B))
def ZU(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def V(A):return min(A for(A,B)in U(A))
def PZ(A,B,C,D):
	K=L(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=X(A);T=Y if C else S
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in T(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def E(A):
	if len(A)==0:return A
	return PG(A,(-V(A),-G(A)))
def PG(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def ZE(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PS(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Z(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PV(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PL(A,B):return PM(ZZ(A,B))
def ZZ(A,B):return type(B)(A(B)for B in B)
def ZJ(A,a,b):return lambda x:A(a(x),b(x))
def PH(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZP(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PW(h,g,f):return lambda x:h(g(f(x)))
def PJ(A,B):return lambda x:A(B(x))
def PU(a,b):return a,b
def PE(A,B):return max(A,key=B)
def PM(A):return type(A)(B for A in A for B in A)
def ZS(A):return len(A)
def P(a,b):return a&b
def PY(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def PP(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def ZX(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));G=PV(I);H=PZ(I,True,False,True);J=PU(5,G);A=ZE(I,(0,0),J);B=Z(H,5);K=PM(B);L=PQ(I,K);M=PJ(U,E);N=ZZ(M,B);C=X(A);O=PS(A,0);Q=PS(A,2);D=ZP(R,10);S=ZP(R,5);T=ZP(P,Q);F=ZP(P,O);W=ZP(P,C);Y=PW(D,ZS,T);a=PW(ZS,F,PR);b=PJ(S,V);c=PW(ZS,F,PX);d=PW(D,ZS,W);e=PJ(PY,Y);f=ZJ(ZX,d,e);g=ZJ(PP,f,c);h=ZJ(PP,g,b);i=ZJ(PP,h,a);j=ZP(ZZ,C);k=PH(PH,PG);l=ZP(PE,i);m=PW(l,j,k);n=PL(m,N);o=ZU(L,1,n);return[*map(list,o)]