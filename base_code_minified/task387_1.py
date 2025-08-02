def p(g):
	G=[]
	for(A,N)in enumerate(g):
		for(B,F)in enumerate(N):
			if F:G.append((B,A,F))
	for(B,A,F)in G:
		for J in(-1,0,1):
			for K in(-1,0,1):g[A+J][B+K]=F if K|J else 5
	L={};M={}
	for(B,A,O)in G:L.setdefault(B,[]).append(A);M.setdefault(A,[]).append(B)
	for(H,C)in L.items():
		if len(C)==2:
			D,I=sorted(C)
			for E in range(D+1,I):
				if E-D&1:g[E][H]=5
	for(H,C)in M.items():
		if len(C)==2:
			D,I=sorted(C)
			for E in range(D+1,I):
				if E-D&1:g[H][E]=5
	return g