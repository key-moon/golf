def p(j,A=range):
	H,I=len(j),len(j[0]);D,E,F,G=H,0,I,0
	for B in A(H):
		for C in A(I):
			if j[B][C]-1:
				if B<D:D=B
				if B>E:E=B
				if C<F:F=C
				if C>G:G=C
	return[[A-(A==1)for A in A[F:G+1]]for A in j[D:E+1]]