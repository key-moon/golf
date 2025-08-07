def PG(A,B):return type(B)(A(B)for B in B)
def PL(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Q(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in U(a)for(C,D)in U(b))
def G(A):return max(A for(A,B)in U(A))
def W(A):return max(A for(B,A)in U(A))
def PM(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(A):return min(A for(B,A)in U(A))
def M(A):return min(A for(A,B)in U(A))
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return G(A)-M(A)+1
def PE(A):return M(A)+PJ(A)//2,K(A)+PX(A)//2
def R(a,b):return Q(a,b)==1
def X(a,b):return len(set(A for(B,A)in U(a))&set(A for(B,A)in U(b)))>0
def V(A,B):
	H,I=PE(A);J,K=PE(B);C,D=0,0
	if X(A,B):C=1 if H<J else-1
	else:D=1 if I<K else-1
	E,F=C,D;G=0
	while not R(A,B)and G<42:G+=1;E+=C;F+=D;A=PV(A,(C,D))
	return E-C,F-D
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PP(A,B,C,D):
	M=L(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=Y if C else Z
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
def PV(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def J(A,n):return frozenset(A for A in A if len(A)==n)
def PU(A,B):return PL(PG(A,B))
def PK(A,a,b):return lambda x:A(a(x),b(x))
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PZ(A,B):return lambda x:A(B(x))
def PY(A):return next(iter(A))
def PS(x):
	if isinstance(x,int):return 0 if x==0 else x+1 if x>0 else x-1
	return 0 if x[0]==0 else x[0]+1 if x[0]>0 else x[0]-1,0 if x[1]==0 else x[1]+1 if x[1]>0 else x[1]-1
def P(a,b):return type(a)(A for A in a if A not in b)
def H(x):return x
def p(I):I=tuple(map(tuple,I));A=PP(I,True,False,True);B=J(A,1);C=P(A,B);D=PY(C);E=PQ(V,D);F=PZ(PS,E);G=PK(PV,H,F);K=PU(G,B);L=PW(I,K);return[*map(list,L)]