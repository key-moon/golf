def p(g):
	J,H=len(g),len(g[0]);C=[[-1]*H for A in g]
	for F in range(J):
		for G in range(H):
			if g[F][G]!=8 and C[F][G]<0:
				K={};I=[(F,G)];C[F][G]=0
				for(A,B)in I:
					L=C[A][B]
					if g[A][B]:K[L]=g[A][B]
					for(D,E)in((A+1,B),(A-1,B),(A,B+1),(A,B-1)):
						if 0<=D<J and 0<=E<H and g[D][E]!=8 and C[D][E]<0:C[D][E]=1-L;I.append((D,E))
				for(A,B)in I:g[A][B]=K[C[A][B]]
	return g