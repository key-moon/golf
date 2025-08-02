def p(g):
	G,F=len(g),len(g[0]);C=max(map(max,g));H=[[0]*F for A in g]
	for A in range(G):
		for D in range(A,G):
			for B in range(F):
				for E in range(B,F):
					if all(g[A][D]==C for A in range(A,D+1)for D in range(B,E+1)):
						if not(A and all(g[A-1][B]==C for B in range(B,E+1))or D<G-1 and all(g[D+1][A]==C for A in range(B,E+1))or B and all(g[A][B-1]==C for A in range(A,D+1))or E<F-1 and all(g[A][E+1]==C for A in range(A,D+1))):
							for I in range(A,D+1):
								for J in range(B,E+1):H[I][J]=C
	return H