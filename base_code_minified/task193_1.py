def p(g):
	F=[[0]*len(g[0])for A in g];G,H=len(g),len(g[0])
	for A in range(G):
		for B in range(H):
			C=g[A][B]
			if C and(A<1 or g[A-1][B]!=C)and(B<1 or g[A][B-1]!=C):
				D=1
				while B+D<H and g[A][B+D]==C:D+=1
				E=1
				while A+E<G and g[A+E][B]==C:E+=1
				if D>1 and E>1 and all(g[A+E][B+F]==C for E in range(E)for F in range(D)):
					for I in range(E):
						for J in range(D):F[A+I][B+J]=C
	return F