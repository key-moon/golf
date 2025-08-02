def p(A):
	for(B,F)in enumerate(A):
		for(C,G)in enumerate(F):
			if G==5:
				for D in(1,0,-1):
					for E in(1,0,-1):
						try:A[B+D][C+E]=A[B+D][C+E]or 1
						except:0
	return A