def p(A):
	I,J=len(A),len(A[0]);B=min(I,J);D=B*B;G=[[0]*D for A in[0]*D]
	for E in range(B):
		for F in range(B):
			H=A[E][F]
			if H:
				K=E*B+B//2;L=F*B+B//2
				for C in range(D):
					if C//B==E or C%B==F:G[C//B*B+B//2][C%B*B+B//2]=H
	return G