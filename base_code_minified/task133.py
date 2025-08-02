def p(g):
	O,P=len(g),len(g[0]);D={}
	for(A,Q)in enumerate(g):
		for(B,E)in enumerate(Q):
			if E:D.setdefault(E,[]).append((A,B))
	for(R,C)in D.items():
		F=[A for(A,B)in C];G=[A for(B,A)in C];H=max(F)-min(F)+1;I=max(G)-min(G)+1
		for(J,K)in((-H,0),(H,0),(0,-I),(0,I)):
			L=1
			for(A,B)in C:
				M,N=A+J,B+K
				if not(0<=M<O and 0<=N<P and g[M][N]==0):L=0;break
			if L:
				for(A,B)in C:g[A+J][B+K]=R
	return g