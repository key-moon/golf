def p(g):
	G,H=len(g),len(g[0]);I=[(A,B)for A in range(G)for B in range(H)if g[A][B]]
	while I:
		A,B=I[0];J=[(A,B)];M=[]
		while J:
			A,B=J.pop()
			if(A,B)in I:I.remove((A,B));M.append((A,B));J+=[(A-1,B),(A+1,B),(A,B-1),(A,B+1)]
		N,O=zip(*M);E,K=min(N),max(N);F,L=min(O),max(O);P=g[E][F];Q=g[E+1][F+1]
		for C in range(E-1,K+2):
			for D in range(F-1,L+2):
				if 0<=C<G and 0<=D<H:g[C][D]=Q
		for C in(E-1,K+1):
			for D in range(F-1,L+2):
				if 0<=C<G and 0<=D<H:g[C][D]=P
		for C in range(E-1,K+2):
			for D in(F-1,L+1):
				if 0<=C<G and 0<=D<H:g[C][D]=P
	return g