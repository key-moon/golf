def p(A):
	G={}
	for(B,I)in enumerate(A):
		for(C,D)in enumerate(I):
			if D:G.setdefault(D,[]).append((B,C))
	for(D,H)in G.items():
		(B,C),(E,F)=H
		if B==E:
			for J in range(min(C,F),max(C,F)+1):A[B][J]=D
	for(D,H)in G.items():
		(B,C),(E,F)=H
		if C==F:
			for K in range(min(B,E),max(B,E)+1):A[K][C]=D
	return A