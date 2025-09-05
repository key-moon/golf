def p(g,z=range):
	D,G=len(g),len(g[0]);E=[]
	for B in z(D-1):
		for A in z(G-1):
			F=g[B][A],g[B][A+1],g[B+1][A],g[B+1][A+1]
			if all(F):E+=[(B,A,len(set(F)))]
	for(B,A,H)in E:
		for I in z(H):
			C=B+2+I
			if C<D:g[C][A]=g[C][A+1]=3
	return g