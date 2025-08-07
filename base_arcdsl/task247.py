def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return tuple(map(min,zip(*J(A))))
def G(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def W(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=L(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def R(A):return next(iter(A))[0]
def Y(A):return min(A for(B,A)in J(A))
def V(A,B,C,D):
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
def PS(A,B):return type(B)(A(B)for B in B)
def PZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def M(a,b):return a,b
def Q(A,B):return B(max(A,key=B,default=0))
def K(A):return type(A)(B for A in A for B in A)
def PJ(A):return len(A)
def H(A,B):return tuple(sorted(A,key=B))
def p(I):I=tuple(map(tuple,I));A=V(I,True,False,True);B=Q(A,PJ);C=S(A,B);D=H(C,Y);E=PS(R,D);F=M(1,B);J=PZ(G,F);L=PS(J,E);N=K(L);O=W(N);return[*map(list,O)]