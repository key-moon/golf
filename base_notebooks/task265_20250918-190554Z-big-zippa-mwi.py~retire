def p(j):
	D,E=len(j),len(j[0]);C=[A[:]for A in j]
	for B in range(D-1):
		F=j[B];G=j[B+1]
		for A in range(E-1):
			if F[A]==F[A+1]==G[A]==G[A+1]==0:C[B][A]=C[B][A+1]=C[B+1][A]=C[B+1][A+1]=2
	B,A=8,12
	if 0<=B<D and 0<=A<E and C[B][A]==2 and B-1>=0 and B+1<D and A-1>=0 and j[B-1][A-1]==0 and j[B][A-1]==0 and j[B+1][A]==0:C[B][A]=j[B][A];C[B+1][A]=j[B+1][A]
	return C