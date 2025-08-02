def p(A):
	for(C,E)in enumerate(A[-1]):
		if E==2:
			try:D=next(A for(A,B)in enumerate(A)if B[C]==5)
			except StopIteration:
				for B in A:B[C]=2
			else:
				for B in A[:D+2]:B[C+1]=2
				for B in A[D+1:]:B[C]=2
	return A