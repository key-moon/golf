def p(g):
	F={}
	for(A,H)in enumerate(g):
		for(B,C)in enumerate(H):
			if C:F.setdefault(C,[]).append((A,B))
	for(C,G)in F.items():
		(A,B),(D,E)=G
		if A==D:
			for I in range(min(B,E),max(B,E)+1):g[A][I]=C
	for(C,G)in F.items():
		(A,B),(D,E)=G
		if B==E:
			for J in range(min(A,D),max(A,D)+1):g[J][B]=C
	return g