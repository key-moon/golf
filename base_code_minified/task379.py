def p(g):
	H,F=len(g),len(g[0]);I=[A.count(8)for A in g];J=[sum(B[A]==8 for B in g)for A in range(F)];G=max(I)>max(J);L=[A for A in(range(H)if G else range(F))if G and I[A]or not G and J[A]]
	for(B,C)in[(A,B)for A in range(H)for B in range(F)if g[A][B]==2]:
		K=(B,C)[not G];A=min(L,key=lambda y:(abs(K-y),K-y))
		if G:
			for D in range(min(B,A),max(B,A)+1):g[D][C]=2
			for D in range(A-1,A+2):
				for E in range(C-1,C+2):
					if 0<=D<H and 0<=E<F:g[D][E]=8
			g[A][C]=2
		else:
			for E in range(min(C,A),max(C,A)+1):g[B][E]=2
			for D in range(B-1,B+2):
				for E in range(A-1,A+2):
					if 0<=D<H and 0<=E<F:g[D][E]=8
			g[B][A]=2
	return g