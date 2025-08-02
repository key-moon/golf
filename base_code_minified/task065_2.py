def p(g):
	A=next(A for A in range(len(g))if len(set(g[A]))==1);B=next(A for A in range(len(g[0]))if len({B[A]for B in g})==1)
	for D in(range(A),range(A+1,len(g))):
		for E in(range(B),range(B+1,len(g[0]))):
			C=[[g[A][B]for B in E]for A in D]
			if len(set(sum(C,[])))>1:return C