def H(A,B):return type(A)(A for A in A if B(A))
def PK(A,B):return type(B)(A(B)for B in B)
def PV(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-W(A)+1
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-X(A)+1
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A):return tuple(map(max,zip(*S(A))))
def M(A):return tuple(map(min,zip(*S(A))))
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return max(A for(B,A)in S(A))
def W(A):return min(A for(B,A)in S(A))
def V(A):return max(A for(A,B)in S(A))
def X(A):return min(A for(A,B)in S(A))
def PQ(A):F,G=X(A)+1,W(A)+1;H,I=V(A)-1,L(A)-1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def Q(A):
	if len(A)==0:return frozenset({})
	B=S(A);C,D=M(B);E,F=G(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def PP(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PU(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def Y(A,B,C):
	G,H=len(A),len(A[0]);I=U(A);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PH(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PM(A):return PY(A)==len(A)and PE(A)==1
def PG(A):return PE(A)==len(A)and PY(A)==1
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
def PZ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def K(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def PL(A,B):return PV(PK(A,B))
def PR(A,a,b):return lambda x:A(a(x),b(x))
def PJ(A,B):return lambda x:A(B(x))
def PS(A,B):return PV(H(A,B))
def PX(a,b):return a or b
def p(I):C=False;I=tuple(map(tuple,I));A=PZ(I,4);D=K(PP,A,A);E=PR(PX,PG,PM);F=PS(D,E);B=Y(I,-1,F);G=R(B,C,C,True);H=PJ(Q,PQ);J=PL(H,G);L=PH(B,2,J);M=PU(L,-1,0);return[*map(list,M)]