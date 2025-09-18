def PM(A,B):return type(B)(A(B)for B in B)
def PE(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return max(A for(B,A)in J(A))
def W(A):return min(A for(B,A)in J(A))
def M(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def R(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PY(A,B):return R(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PS(A):F,G=L(A)-1,W(A)-1;H,I=M(A)+1,Y(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def V(A,B,C):
	H,I=len(A),len(A[0]);K=E(A);D=list(list(A)for A in A)
	for(F,G)in J(C):
		if 0<=F<H and 0<=G<I:
			if D[F][G]==K:D[F][G]=B
	return tuple(tuple(A)for A in D)
def PQ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Q(A,B,C,D):
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
def H(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-W(A)+1
def PJ(A,B):return PE(PM(A,B))
def PW(A,n):
	if n==1:return A
	return PZ(A,PW(A,n-1))
def PV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PP(A,B):return lambda x:A(x)==B
def PZ(A,B):return lambda x:A(B(x))
def G(A,B):return type(A)(A for A in A if B(A))
def K(a,b):return a>b
def PX(n):return n//2 if isinstance(n,int)else(n[0]//2,n[1]//2)
def p(I):B=True;I=tuple(map(tuple,I));D=Q(I,B,B,B);E=H(I,9);A=P(D,9);F=PV(PY,(1,0));J=PJ(F,E);L=V(I,1,J);C=PZ(PX,PU);M=PV(K,1);N=PZ(M,C);O=PP(C,3);R=PW(PS,2);S=PW(PS,3);T=PJ(PS,A);U=G(A,N);W=G(A,O);X=PJ(R,U);Y=PJ(S,W);Z=PQ(L,3,T);a=PQ(Z,3,X);b=PQ(a,3,Y);return[*map(list,b)]