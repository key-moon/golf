def p(g):
	for A in g:
		try:B,D=next((B,A)for(B,A)in enumerate(A)if A)
		except:continue
		for C in range(len(A)-B):A[B+C]=[D,5][C&1]
	return g