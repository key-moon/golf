def p(A):
	for B in{A for B in A for A in B if A}:
		C=[(A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B];D,E=zip(*C)
		if len(C)!=(max(D)-min(D)+1)*(max(E)-min(E)+1):return[[B]]