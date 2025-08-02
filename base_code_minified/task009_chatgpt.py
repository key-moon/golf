def p(g):
	I,Q=len(g),len(g[0]);J=max(set(A for B in g for A in B if A),key=lambda x:sum(A.count(x)for A in g));C=[-1]+[A for A in range(I)if all(A==J for A in g[A])]+[I];D=[-1]+[A for A in range(Q)if all(g[B][A]==J for B in range(I))]+[Q];F=[[0]*(len(D)-1)for A in range(len(C)-1)]
	for E in range(len(C)-1):
		for A in range(len(D)-1):
			for K in range(C[E]+1,C[E+1]):
				for L in range(D[A]+1,D[A+1]):
					M=g[K][L]
					if M and M!=J:F[E][A]=M
	for G in F:
		for B in set(G):
			if B:
				N=min(A for(A,C)in enumerate(G)if C==B);O=max(A for(A,C)in enumerate(G)if C==B)
				for H in range(N,O+1):
					if G[H]==0:G[H]=B
	for A in range(len(D)-1):
		P=[F[B][A]for B in range(len(C)-1)]
		for B in set(P):
			if B:
				N=min(A for(A,C)in enumerate(P)if C==B);O=max(A for(A,C)in enumerate(P)if C==B)
				for H in range(N,O+1):
					if F[H][A]==0:F[H][A]=B
	for E in range(len(C)-1):
		for A in range(len(D)-1):
			if F[E][A]:
				for K in range(C[E]+1,C[E+1]):
					for L in range(D[A]+1,D[A+1]):g[K][L]=F[E][A]
	return g