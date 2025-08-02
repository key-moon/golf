def p(A):
	N=len(A);C=N//3;B=C+1;L=A[C][C];H=[[any(A[D*B+F][E*B+G]for F in range(C)for G in range(C))for E in range(3)]for D in range(3)]
	for F in range(3):
		for G in range(3):
			if not H[F][G]:
				I=[A for A in range(3)if H[F][A]]
				if len(I)>1:
					J,K=I[0],I[1]
					for D in range(C):
						for E in range(C):
							if A[F*B+D][J*B+E]or A[F*B+D][K*B+E]:A[F*B+D][G*B+E]=L
				else:
					M=[A for A in range(3)if H[A][G]];J,K=M[0],M[1]
					for D in range(C):
						for E in range(C):
							if A[J*B+D][G*B+E]or A[K*B+D][G*B+E]:A[F*B+D][G*B+E]=L
	return A