def p(g):
	B=range;A=(len(g)-1)//2
	if A==1:
		D=[g[0][0],g[0][2],g[2][0],g[2][2]]
		for C in D:
			if D.count(C)==1:return[[C]]
	for(F,G)in[(0,0),(0,A+1),(A+1,0),(A+1,A+1)]:
		E=[[g[F+C][G+A]for A in B(A)]for C in B(A)];C=[E[C][D]for C in B(A)for D in B(A)]
		if len(set(C))>1:return E