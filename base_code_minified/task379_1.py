def p(A):
	J,K=len(A),len(A[0]);G=[A for(A,B)in enumerate(A)if min(B)==8];H=[B for B in range(K)if min(A[C][B]for C in range(J))==8];L=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==2]
	for(B,C)in L:
		D=min(G,key=lambda N:abs(N-B))if G else 0;F=min(H,key=lambda N:abs(N-C))if H else 0
		if G and(not H or abs(B-D)<=abs(C-F)):
			for E in range(min(B,D),max(B,D)+1):A[E][C]=2
			for E in range(C-1,C+2):
				for I in(D-1,D,D+1):A[I][E]=8
			A[D][C]=2
		else:
			for E in range(min(C,F),max(C,F)+1):A[B][E]=2
			for E in range(F-1,F+2):
				for I in(B-1,B,B+1):A[I][E]=8
			A[B][F]=2
	return A