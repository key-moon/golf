def p(g):
	H,I=len(g),len(g[0]);J={}
	for A in range(H):
		for B in range(I):
			D=g[A][B]
			if D:J.setdefault(D,[]).append((A,B))
	E=[[0]*I for A in range(H)]
	for(D,C)in J.items():
		F=max({A for(A,B)in C},key=lambda u:sum(A==u for(A,B)in C));K=sum(A==F for(A,B)in C);G=max({A for(B,A)in C},key=lambda v:sum(A==v for(B,A)in C));L=sum(A==G for(B,A)in C)
		if K+L>2:
			if L>K:
				for(A,B)in C:
					if B==G:E[A][B]=D
					else:E[A][G+(B>G and 1 or-1)]=D
			else:
				for(A,B)in C:
					if A==F:E[A][B]=D
					else:E[F+(A>F and 1 or-1)][B]=D
	return E