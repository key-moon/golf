def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def U(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def L(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def X(A,B,C,D):
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
def V(A,a,b):return a if A else b
def Y(A,B):return B(max(A,key=B,default=0))
def M(A):return len(A)
def E(a,b):return a==b
def p(I):B=False;I=tuple(map(tuple,I));C=X(I,True,B,B);A=Y(C,M);D=E(A,1);F=E(A,4);G=E(A,5);H=V(D,2,1);J=V(F,3,H);K=V(G,6,J);N=L(K,(1,1));return[*map(list,N)]