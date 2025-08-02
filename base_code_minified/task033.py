def p(A):
	B=len(A)//3;E=A[B][0]
	for F in range(3):
		for G in range(3):
			if F^G&1:
				H=F*(B+1);I=G*(B+1)
				for C in range(B):
					for D in range(B):
						if A[C][D]&A[C][D]-E and not A[H+C][I+D]:A[H+C][I+D]=E
	return A