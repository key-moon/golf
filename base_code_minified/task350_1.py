def p(A):
	for E in A:
		B=-1
		for(C,G)in enumerate(E):
			if G:
				if B+1:
					for D in range(B+1,C):E[D]=E[D]or 8
				B=C
	H=len(A)
	for F in range(len(A[0])):
		B=-1
		for C in range(H):
			if A[C][F]:
				if B+1:
					for D in range(B+1,C):A[D][F]=A[D][F]or 8
				B=C
	return A