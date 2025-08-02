def p(g):
	G=len(g);H=len(g[0]);K=[A[:]for A in g]
	for A in range(G):
		for B in range(H):
			if g[A][B]==2:
				C=A
				while C and g[C-1][B]==3:C-=1
				D=A
				while D<G-1 and g[D+1][B]==3:D+=1
				E=B
				while E and g[A][E-1]==3:E-=1
				F=B
				while F<H-1 and g[A][F+1]==3:F+=1
				I=(A==C)*-1+(A==D);J=(B==E)*-1+(B==F);O=I and(A if I<0 else G-1-A)or J and(B if J<0 else H-1-B)
				for L in range(1,O+1):
					for M in range(C,D+1):
						for N in range(E,F+1):K[M+I*L][N+J*L]=g[M][N]
	return K