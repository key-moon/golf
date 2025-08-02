def p(val_g):
	A=val_g;I,F=len(A),len(A[0]);G=[[0]*F for A in A]
	for B in range(1,I-1):
		for C in range(1,F-1):
			H=A[B][C]
			if H and A[B-1][C]==A[B+1][C]==A[B][C-1]==A[B][C+1]:
				J=A[B-1][C]
				for D in range(-2,3):
					for E in range(-2,3):
						if D|E and(D*E==0 or abs(D)==abs(E)):G[B+D][C+E]=H if abs(D)==abs(E)else J
	return G