def p(g):
	for A in g:
		B=[A for(A,B)in enumerate(A)if B]
		if B:
			D,E=B;F=sum(B)//2
			for C in range(D+1,E):A[C]=[A[D],5,A[E]][(C>F)+(C>=F)]
	return g