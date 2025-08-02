def p(A):
	L,K=len(A),len(A[0]);F=L;G=-1;D=K;E=-1
	for(B,I)in enumerate(A):
		for(C,J)in enumerate(I):
			if J==5:
				if B<F:F=B
				if B>G:G=B
				if C<D:D=C
				if C>E:E=C
	H=[[0]*K for A in A]
	for B in range(F,G+1):H[B][D:E+1]=[5]*(E-D+1)
	if G-F>E-D:
		for(B,I)in enumerate(A):
			for(C,J)in enumerate(I):
				if J%5:
					if C<D:H[B][D-1]=5
					if C>E:H[B][E+1]=5
	else:
		for(B,I)in enumerate(A):
			for(C,J)in enumerate(I):
				if J%5:
					if B<F:H[F-1][C]=5
					if B>G:H[G+1][C]=5
	return H