def p(A):
	F=len(A);C=next(A for(A,B)in enumerate(A)if B[0]==5)
	for(B,G)in enumerate(A):
		for(H,D)in enumerate(G):
			if 0<D<5:
				if D^1:E=range(B+1,C)if B<C else range(C+1,B)
				else:E=range(B)if B<C else range(B+1,F)
				for I in E:A[I][H]=D
	return A