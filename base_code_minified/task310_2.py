def p(g):
	for A in range(1,min(len(g),len(g[0]))):
		B={}
		for C in range(0,len(g)-A+1,A):
			for D in range(0,len(g[0])-A+1,A):E=tuple(tuple(g[B][D:D+A])for B in range(C,C+A));B[E]=B.get(E,0)+1
		F=B.values()
		if len({*F})>1:G=min(F);return[list(A)for(A,B)in B.items()if B==G][0]