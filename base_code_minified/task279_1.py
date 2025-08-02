def p(g):
	G=len(g);H=len(g[0]);C=[[0]*H for A in range(G)];I=[]
	for D in range(G):
		for E in range(H):
			if g[D][E]==1 and not C[D][E]:
				F=[(D,E)];C[D][E]=1
				for(J,K)in F:
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
						A=J+L;B=K+M
						if 0<=A<G and 0<=B<H and g[A][B]==1 and not C[A][B]:C[A][B]=1;F.append((A,B))
				if len(F)>len(I):I=F
	for(J,K)in I:g[J][K]=8
	return g