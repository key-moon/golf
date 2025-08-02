def p(A):
	C,H=len(A),len(A[0])
	for B in A:
		for I in B:
			if I:F=I;break
		else:continue
		break
	D=C
	for(J,B)in enumerate(A):
		E=[A for(A,B)in enumerate(B)if B==F]
		if len(E)>1:D=J;break
		if E and D==C:D=J
	G=(C-D)%2==0
	for L in range(C,H):
		B=[0]*H
		if G:
			for K in E:B[K]=F
		else:B[E[-1]]=F
		A.append(B);G=not G
	return A