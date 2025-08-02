def p(g):
	H,I=len(g),len(g[0])
	for D in range(H):
		for E in range(I):
			if g[D][E]==3:
				A=[(D,E)];g[D][E]=0
				for(F,G)in A:
					for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
						B=F+J;C=G+K
						if 0<=B<H and 0<=C<I and g[B][C]==3:A.append((B,C));g[B][C]=0
				for(F,G)in A:g[F][G]=8 if len(A)>2 else 3
	return g