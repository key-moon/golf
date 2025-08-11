def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return S(A)|U(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def L(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Q(A):return max(A for(A,B)in X(A))
def M(A):return min(A for(A,B)in X(A))
def W(A):return max(A for(B,A)in X(A))
def K(A):return min(A for(B,A)in X(A))
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-M(A)+1
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def X(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PY(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def G(A):return tuple(map(min,zip(*X(A))))
def PU(A):return PZ(A),PJ(A)
def PS(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def H(A,B):return PY(B,G(A),PU(A))
def R(A,B,C,D):
	K=Y(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=L(A);T=V if C else S
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
def E(A,n):return frozenset(A for A in A if len(A)==n)
def Z(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PL(A,B):return type(B)(A(B)for B in B)
def PX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PP(A,B):return max(A,key=B)
def P(a,b):return type(a)(A for A in a if A not in b)
def p(I):B=False;I=tuple(map(tuple,I));C=J(I);A=R(I,True,B,B);D=E(A,1);F=P(A,D);G=PX(H,I);K=PL(G,F);L=PX(Z,C);M=PP(K,L);N=Y(M);O=PS(N,(1,1));return[*map(list,O)]