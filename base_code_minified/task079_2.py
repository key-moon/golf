def p(g):
	C=max({A for B in g for A in B if A},key=lambda c:sum(A.count(c)for A in g));D=sum(A.count(C)for A in g)//3;E,F=len(g),len(g[0])
	for A in range(E-2):
		for B in range(F-2):
			G=sum(g[A+D][B+E]==C for D in(0,1,2)for E in(0,1,2))
			if G==D and all(g[A+D][B+E]in(0,C)for D in(0,1,2)for E in(0,1,2)):return[A[B:B+3]for A in g[A:A+3]]