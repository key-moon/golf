def p(A):
	N=[(B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A];C,D,G=N[0];E,H,I=N[1]
	if C==E:
		J=C;L=1 if H>D else-1;F=(H-D)*L//2;O=(D+H)//2
		for B in range(F+1):A[J][D+L*B]=G;A[J][H-L*B]=I
		for B in range(1,F+1):A[J-B][O]=G;A[J+B][O]=I
	else:
		K=D;M=1 if E>C else-1;F=(E-C)*M//2;P=(C+E)//2
		for B in range(F+1):A[C+M*B][K]=G;A[E-M*B][K]=I
		for B in range(1,F+1):A[P][K-B]=G;A[P][K+B]=I
	return A