from collections import Counter
def p(g):
	N,O=len(g),len(g[0]);P=[B for A in g for B in A];Q=Counter(P).most_common(1)[0][0];B=[(A,B)for A in range(N)for B in range(O)if g[A][B]!=Q]
	if not B:return[A[:]for A in g]
	def J(grid):A=[B for A in grid for B in A];return min(set(A),key=A.count)
	def K(grid,a,b):return tuple(tuple(b if A==a else A for A in A)for A in grid)
	L=K(g,8,0);M=J(L);C=J(K(L,M,0));F=min(A for(A,B)in B);G=max(A for(A,B)in B);H=min(A for(B,A)in B);I=max(A for(B,A)in B);A=[A[:]for A in g]
	for D in range(F,G+1):
		for E in range(H,I+1):A[D][E]=M
	for E in range(H,I+1):A[F][E]=C;A[G][E]=C
	for D in range(F,G+1):A[D][H]=C;A[D][I]=C
	return A