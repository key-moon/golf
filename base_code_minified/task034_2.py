def p(g):
	B=len(g)
	for C in range(B):
		for D in range(B):
			if g[C][D]==2:
				J=[(A,E)for(A,E)in((1,0),(-1,0),(0,1),(0,-1))if 0<=C+A<B and 0<=D+E<B and g[C+A][D+E]>2];A,E=J;I=-A[0]-E[0],-A[1]-E[1];K=g[C+A[0]][D+A[1]];F=0
				while 1:
					for(L,M)in(A,E,(A[0]+E[0],A[1]+E[1])):
						G=C+L+F*I[0];H=D+M+F*I[1]
						if G<0 or G>=B or H<0 or H>=B:return g
						g[G][H]=K
					F+=1