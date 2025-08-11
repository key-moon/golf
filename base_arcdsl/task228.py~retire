def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def G(A):return tuple(map(max,zip(*J(A))))
def H(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*J(A)))))
def K(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*J(A)))))
def W(A):return tuple(map(min,zip(*J(A))))
def ZZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return max(A for(B,A)in J(A))
def Q(A):return min(A for(B,A)in J(A))
def M(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def PX(A):F,G=L(A)-1,Q(A)-1;H,I=M(A)+1,Y(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def PM(A,B):return ZZ(A,E(A),J(B))
def PP(A):return frozenset({W(A),K(A),H(A),G(A)})
def PG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PY(A):return next(iter(A))[0]
def V(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def PS(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();Q,R=len(A),len(A[0]);S=U(A);T=X if C else P
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def S(A,n):return frozenset(A for A in A if len(A)==n)
def PR(A,B):return type(B)(A(B)for B in B)
def ZP(A,a,b):return lambda x:A(a(x),b(x))
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PK(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PV(h,g,f):return lambda x:h(g(f(x)))
def PJ(A,B):return lambda x:A(B(x))
def PU(a,b):return a,b
def PZ(A):return frozenset({A})
def PE(A,B):return max(A,key=B)
def PL(A):return type(A)(B for A in A for B in A)
def PH(A):return len(A)
def R(x):return x
def p(I):I=tuple(map(tuple,I));A=PS(I,True,False,True);B=S(A,1);C=PE(A,PH);D=PX(C);E=PP(D);F=PQ(PK,V);G=PQ(PE,B);H=PV(G,F,PZ);J=PJ(PY,H);K=ZP(PU,J,R);L=PR(K,E);M=PL(B);N=PM(I,M);O=PG(N,L);return[*map(list,O)]