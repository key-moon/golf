def p(A):
	for B in range(len(A)-2):
		for C in range(len(A[0])-2):
			if not any(A[B+D][C+E]for D in(0,1,2)for E in(0,1,2)):
				for D in(0,1,2):
					for E in(0,1,2):A[B+D][C+E]=1
				return A