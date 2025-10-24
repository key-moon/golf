def p(t):
	D,D=len(t),len(t[0]);C=[A[:]for A in t]
	for B in range(D-1):
		E=t[B];F=t[B+1]
		for A in range(D-1):
			if E[A]==E[A+1]==F[A]==F[A+1]==0:C[B][A]=C[B][A+1]=C[B+1][A]=C[B+1][A+1]=2
	B,A=8,12
	if 0<=B<D and t[B-1][A-1]==0 and t[B][A-1]==0 and t[B+1][A]==0:C[B][A]=t[B][A];C[B+1][A]=t[B+1][A]
	return C