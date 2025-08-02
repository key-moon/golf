def p(A):
	C=len(A);E=len(A[0]);B=[0]*E
	for D in range(E):
		while B[D]<C and A[C-1-B[D]][D]==5:B[D]+=1
	H=[A for A in B if A];F=max(B);G=min(H);I=B.index(F);J=B.index(G);return[[1 if B==I and A>=C-F else 2 if B==J and A>=C-G else 0 for B in range(E)]for A in range(C)]