def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def U(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def V(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Y(A,B,C,D):
	L=S(A)if D else None;M=set();G=set();Q,R=len(A),len(A[0]);T=J(A);V=U if C else P
	for E in T:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==L:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				K=A[F[0]][F[1]]
				if H==K if B else K!=L:N.add((K,F));G.add(F);O|={(A,B)for(A,B)in V(F)if 0<=A<Q and 0<=B<R}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def G(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def L(A,B):return lambda x:A(B(x))
def Q(A,a,b):return a if A else b
def M(A,B):return type(A)(A for A in A if B(A))
def K(A):return len(A)
def X(a,b):return a>b
def E(A,B):return A in B
def p(I):I=tuple(map(tuple,I));A=Y(I,False,True,True);B=G(E,2);C=L(B,V);D=M(A,C);F=K(D);H=X(F,1);J=Q(H,0,8);N=W(J,(1,1));return[*map(list,N)]