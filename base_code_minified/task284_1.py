def p(val_g):
	B=val_g;N=[(B,D,A)for(B,C)in enumerate(B)for(D,A)in enumerate(C)if A];C,D,G=N[0];E,H,I=N[1]
	if C==E:
		J=C;L=1 if H>D else-1;F=(H-D)*L//2;O=(D+H)//2
		for A in range(F+1):B[J][D+L*A]=G;B[J][H-L*A]=I
		for A in range(1,F+1):B[J-A][O]=G;B[J+A][O]=I
	else:
		K=D;M=1 if E>C else-1;F=(E-C)*M//2;P=(C+E)//2
		for A in range(F+1):B[C+M*A][K]=G;B[E-M*A][K]=I
		for A in range(1,F+1):B[P][K-A]=G;B[P][K+A]=I
	return B