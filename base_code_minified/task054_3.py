def p(A):
	F={B for A in A for B in A};G=len(A);H=len(A[0])
	for B in range(1,G-1):
		for C in range(1,H-1):
			D=A[B][C];E=A[B-1][C]
			if D!=E==A[B+1][C]==A[B][C-1]==A[B][C+1]:
				I=min(F-{E,D})
				for(J,K)in[(-1,-1),(-1,1),(1,-1),(1,1)]:A[B+J][C+K]=I
	return A