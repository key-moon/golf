def p(A):
	F=next(A for A in A if 0 not in A);D=[]
	for B in F:
		if B not in D:D+=[B]
	for E in A:
		C=[]
		for B in E:
			if B and B not in C:C+=[B]
		if C and 0 in E:
			for(G,B)in enumerate(F):E[G]=C[D.index(B)]
	return A