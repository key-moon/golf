def p(A):
	D=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==1];B,C=map(min,zip(*D));E,F=map(max,zip(*D));I=[(A-B,D-C)for(A,D)in D];J=[(D-B,E-C)for D in range(B,E+1)for E in range(C,F+1)if A[D][E]==4];K,L=E-B+1,F-C+1
	for G in range(len(A)-K+1):
		for H in range(len(A[0])-L+1):
			if all(A[G+B][H+C]==4 for(B,C)in J):
				for(M,N)in I:A[G+M][H+N]=1
	return A