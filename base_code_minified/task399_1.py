def p(g):
	E=[[0]*3 for A in[0]*3];I=[(0,0),(0,2),(1,1),(2,0),(2,2)];D=len(g);F=0
	for G in range(D):
		for H in range(D):
			if g[G][H]==2:
				J,K=I[F];E[J][K]=1;F+=1;C=[(G,H)]
				while C:
					A,B=C.pop()
					if g[A][B]!=2:continue
					g[A][B]=0
					if A:C+=[(A-1,B)]
					if A+1<D:C+=[(A+1,B)]
					if B:C+=[(A,B-1)]
					if B+1<D:C+=[(A,B+1)]
	g=E;return g