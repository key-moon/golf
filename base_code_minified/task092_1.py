def p(g):
	H={}
	for(A,I)in enumerate(g):
		for(B,C)in enumerate(I):
			if C:H.setdefault(C,[]).append((A,B))
	for(C,J)in H.items():
		(D,E),(F,G)=J
		for A in range(min(D,F),max(D,F)+1):
			for B in range(min(E,G),max(E,G)+1):
				if g[A][B]==0 and(A==D or A==F or B==E or B==G):g[A][B]=C
	return g