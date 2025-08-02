def p(g):
	B=0
	for(I,F)in enumerate(g):
		if 1 in F:
			A=F.index(1);K=len(F)-1-F[::-1].index(1)
			if not B:L=I;G=A;H=K;B=1
			else:G=min(G,A);H=max(H,K)
		elif B:
			C=(L+I-1)//2;D=(G+H)//2
			for(A,J)in enumerate(g[C]):
				if J!=1:g[C][A]=6
			for E in g:
				if E[D]!=1:E[D]=6
			B=0
	if B:
		C=(L+I)//2;D=(G+H)//2
		for(A,J)in enumerate(g[C]):
			if J!=1:g[C][A]=6
		for E in g:
			if E[D]!=1:E[D]=6
	return g