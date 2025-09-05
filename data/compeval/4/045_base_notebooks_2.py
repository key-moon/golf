def	p(j):
	for	A	in	j:
		for	c	in{*A}-{0}:
			C=A.index(c);k=len(A)-A[::-1].index(c)
			for	B	in	range(C,k):
				if~A[B]:A[B]=c
	return	j