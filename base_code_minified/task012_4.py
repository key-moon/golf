def p(A):
	F=[[0]*len(A[0])for B in A]
	for B in range(2,len(A)-2):
		for C in range(2,len(A[0])-2):
			G=A[B][C];H=A[B-1][C]
			if G*H*A[B+1][C]*A[B][C-1]*A[B][C+1]:
				for D in range(-2,3):
					for E in range(-2,3):F[B+D][C+E]=H if not D*E and abs(D)+abs(E)>0 else G
	return F