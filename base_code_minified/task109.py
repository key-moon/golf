def p(g):
	for(I,F)in enumerate(g):
		if len({*F})==1 and F[0]:H=F[0];break
	J=next(A for A in range(len(g[0]))if all(g[B][A]==H for B in range(len(g))));G=[A[:J]for A in g[:I]];D=len(G);E=len(G[0]);A=[[0]*(2*E)for A in range(2*D)]
	for B in range(D):
		for C in range(E):
			if G[B][C]:A[B][C]=A[B][2*E-1-C]=A[2*D-1-B][C]=A[2*D-1-B][2*E-1-C]=H
	return A