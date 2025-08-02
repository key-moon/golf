def p(A):
	H,G=len(A),len(A[0]);B=[0]*5
	for C in range(G):
		for F in range(C,G):
			D=0
			for(E,I)in enumerate(A+[[]]):
				if E<H and all(A==0 for A in I[C:F+1]):D+=1;continue
				if(J:=D*(F-C+1))>B[0]:B=[J,E-D,C,D,F-C+1]
				D=0
	for E in range(B[3]):A[B[1]+E][B[2]:B[2]+B[4]]=[6]*B[4]
	return A