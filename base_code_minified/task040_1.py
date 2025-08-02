def p(A):
	F=len(A);D=F-1;G=len(set(A[0]))==1
	for(E,C)in enumerate(A):
		for(B,H)in enumerate(C):
			if H==3:C[B]=(A[0][B]if E<D-E else A[-1][B])if G else C[0]if B<D-B else C[-1]
	return A