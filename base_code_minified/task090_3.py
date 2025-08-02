def p(g):
	G,F=len(g),len(g[0]);A=[0]*5
	for B in range(F):
		for E in range(B,F):
			C=0
			for(D,H)in enumerate(g+[[]]):
				if D<G and all(A==0 for A in H[B:E+1]):C+=1;continue
				if(I:=C*(E-B+1))>A[0]:A=[I,D-C,B,C,E-B+1]
				C=0
	for D in range(A[3]):g[A[1]+D][A[2]:A[2]+A[4]]=[6]*A[4]
	return g