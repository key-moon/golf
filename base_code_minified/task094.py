def p(A):
	G,F=len(A),len(A[0])
	for C in range(G):
		for B in range(F):
			if A[C][B]==1 and(C<1 or A[C-1][B]!=1)and(B<1 or A[C][B-1]!=1):
				D=1
				while B+D<F and A[C][B+D]==1:D+=1
				H=C+D//2;I=B+D//2
				for E in range(G):
					if A[E][I]==8:A[E][I]=6
				for E in range(F):
					if A[H][E]==8:A[H][E]=6
	return A