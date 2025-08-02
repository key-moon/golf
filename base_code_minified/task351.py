def p(A):
	E=F=D=0;G=len(A)-4
	for C in range(G):
		for B in range(G):
			H=len({*A[C][B:B+5],*A[C+1][B:B+5],*A[C+2][B:B+5],*A[C+3][B:B+5],*A[C+4][B:B+5]})
			if H>E:E,F,D=H,C,B
	return[A[F+B][D:D+5][::-1]for B in range(5)]