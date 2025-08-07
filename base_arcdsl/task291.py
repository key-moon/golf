def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def R(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def M(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def G(A):return next(iter(A))[0]
def L(a,b):return U(a,b)==1
def Y(A,B,C,D):
	L=S(A)if D else None;M=set();H=set();Q,R=len(A),len(A[0]);T=E(A);U=X if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in U(G)if 0<=A<Q and 0<=B<R}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def K(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def Q(A,B):return type(B)(B for B in B if B!=A)
def V(A,B):return next(A for A in A if B(A))
def W(A,B):return min(A,key=B)
def H(A):return len(A)
def p(I):C=False;I=tuple(map(tuple,I));A=Y(I,True,C,C);B=W(A,H);D=K(L,B);E=Q(B,A);F=V(E,D);J=G(F);N=M(J,(1,1));return[*map(list,N)]