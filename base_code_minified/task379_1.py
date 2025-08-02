def p(g):
	I,J=len(g),len(g[0]);F=[A for(A,B)in enumerate(g)if min(B)==8];G=[A for A in range(J)if min(g[B][A]for B in range(I))==8];K=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==2]
	for(A,B)in K:
		C=min(F,key=lambda x:abs(x-A))if F else 0;E=min(G,key=lambda x:abs(x-B))if G else 0
		if F and(not G or abs(A-C)<=abs(B-E)):
			for D in range(min(A,C),max(A,C)+1):g[D][B]=2
			for D in range(B-1,B+2):
				for H in(C-1,C,C+1):g[H][D]=8
			g[C][B]=2
		else:
			for D in range(min(B,E),max(B,E)+1):g[A][D]=2
			for D in range(E-1,E+2):
				for H in(A-1,A,A+1):g[H][D]=8
			g[A][E]=2
	return g