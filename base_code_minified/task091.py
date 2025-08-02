def p(A):
	B=0,0,0,0;G,H=len(A),len(A[0])
	for E in range(H):
		for F in range(E+1,H):
			for C in range(G):
				if A[C][E]==A[C][F]!=0:
					D=1
					while C+D<G and A[C+D][E]==A[C+D][F]!=0:D+=1
					if D>B[0]:B=D,C,E,F
	return[A[B[2]:B[3]+1]for A in A[B[1]:B[1]+B[0]]]