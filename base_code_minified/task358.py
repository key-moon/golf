def p(A):
	C,F=len(A),len(A[0])
	for B in range(C):
		D=[C for C in range(F)if A[B][C]]
		if len(D)>1:
			G=D[0];H=len(D);L=[A[B][G+C]for C in range(H)];E=next(D for D in D if B and A[B-1][D]or B+1<C and A[B+1][D]);I=[A[B][E]for B in range(C)if A[B][E]];M=min(B for B in range(C)if A[B][E])
			for J in range(C):A[J][E]=I[(J-M)%len(I)]
			for K in range(F):A[B][K]=L[(K-G)%H]
			break
	return A