def p(g):
	for C in g:
		if(A:=[A for(A,B)in enumerate(C)if B==8])[1:]:
			for B in range(A[0]+1,A[-1]):C[B]=3
	for(D,E)in enumerate(zip(*g)):
		if(A:=[A for(A,B)in enumerate(E)if B==8])[1:]:
			for B in range(A[0]+1,A[-1]):g[B][D]=3
	return g