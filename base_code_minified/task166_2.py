def p(val_g):
	C=val_g;D,E=len(C),len(C[0]);F=[(A,B)for A in range(D)for B in range(E)if A*B*(D-1-A)*(E-1-B)==0 and C[A][B]==0]
	while F:
		A,B=F.pop()
		if C[A][B]==0:C[A][B]=-1;F+=(A+1,B),(A-1,B),(A,B+1),(A,B-1)
	for A in range(D):
		for B in range(E):
			if C[A][B]==0:C[A][B]=2
			elif C[A][B]<0:C[A][B]=0
	return C