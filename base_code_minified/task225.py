def p(A):
	for H in range(5):
		for I in range(5):
			if A[H][I]and A[H][I+1]and A[H+1][I]and A[H+1][I+1]:D,E=H,I;break
		else:continue
		break
	J=A[D][E];K=A[D][E+1];L=A[D+1][E];M=A[D+1][E+1]
	for(F,G)in((0,0),(0,1),(1,0),(1,1)):
		B,C=D-1-F,E-1-G
		if 0<=B<6 and 0<=C<6 and A[B][C]==0:A[B][C]=M
	for(F,G)in((0,0),(0,1),(1,0),(1,1)):
		B,C=D-1-F,E+2+G
		if 0<=B<6 and 0<=C<6 and A[B][C]==0:A[B][C]=L
	for(F,G)in((0,0),(0,1),(1,0),(1,1)):
		B,C=D+2+F,E-1-G
		if 0<=B<6 and 0<=C<6 and A[B][C]==0:A[B][C]=K
	for(F,G)in((0,0),(0,1),(1,0),(1,1)):
		B,C=D+2+F,E+2+G
		if 0<=B<6 and 0<=C<6 and A[B][C]==0:A[B][C]=J
	return A