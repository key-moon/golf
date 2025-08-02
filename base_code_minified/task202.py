def p(g):
	I,J=len(g),len(g[0]);K=[(A,B)for A in range(I)for B in range(J)if g[A][B]==0]
	for G in set(sum(g,[]))-{0}:
		H=[A for A in range(I)if G in g[A]];L=[A for A in range(J)if any(g[B][A]==G for B in H)];A,B=H[0],H[-1];C,D=L[0],L[-1];M={E for(E,F)in K if A<=E<=B and C<=F<=D};N={E for(F,E)in K if A<=F<=B and C<=E<=D}
		if N and D-C>B-A:
			for E in range(A,B+1):
				for F in N:
					if g[E][F]==G:g[E][F]=0
		if M and B-A>=D-C:
			for E in M:
				for F in range(C,D+1):
					if g[E][F]==G:g[E][F]=0
	return g