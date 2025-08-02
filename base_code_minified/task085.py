def p(A):
	for F in range(1,len(A)-1):
		G,C,H=A[F-1],A[F],A[F+1];B=-1
		for D in range(len(C)):
			if C[D]and G[D]==C[D]==H[D]:
				if B<0:B=D
			elif B>=0:
				for E in range(D-B):
					if E&1:C[B+E]=0
				B=-1
		if B>=0:
			for E in range(len(C)-B):
				if E&1:C[B+E]=0
	return A