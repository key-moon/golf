def _most_color(grid):
	A={}
	for C in grid:
		for B in C:A[B]=A.get(B,0)+1
	return max(A,key=A.get)
def solve_c8cbb738(I):
	R,S=len(I),len(I[0]);N=_most_color(I);C={}
	for D in range(R):
		for E in range(S):
			A=I[D][E]
			if A==N:continue
			C.setdefault(A,[]).append((D,E))
	if not C:return I
	F={}
	for(A,B)in C.items():G=[A[0]for A in B];H=[A[1]for A in B];J=max(G)-min(G)+1;K=max(H)-min(H)+1;F[A]=J,K
	L=max(A for(A,B)in F.values());M=max(A for(B,A)in F.values());O=[[N]*M for A in range(L)]
	for(A,B)in C.items():
		G=[A[0]for A in B];H=[A[1]for A in B];T,U=min(G),min(H);J,K=F[A];V=(L-J)//2;W=(M-K)//2
		for(D,E)in B:
			P=D-T+V;Q=E-U+W
			if 0<=P<L and 0<=Q<M:O[P][Q]=A
	return tuple(tuple(A)for A in O)
def p(g):A=tuple(tuple(A)for A in g);B=solve_c8cbb738(A);return[list(A)for A in B]
