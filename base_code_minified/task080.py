def p(A):
	G=[A for(A,B)in enumerate(A)if len(set(B))==1];H=[B for B in range(len(A[0]))if len({A[C][B]for C in range(len(A))})==1];B=[0]+G+[len(A)];D=[0]+H+[len(A[0])];I=[[[A[D[E]:D[E+1]]for A in A[B[C]:B[C+1]]]for E in range(len(D)-1)]for C in range(len(B)-1)];L=list(map(list,zip(*I)));E=[]
	for C in val_bt:
		for J in range(len(C[0])):
			F=[]
			for K in C:F+=K[J]
			E.append(F)
		if B[val_bt.index(C)+1]<len(A):E.append(A[B[val_bt.index(C)+1]])
	return E