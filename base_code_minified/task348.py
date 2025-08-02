def p(g):
	C,D=next((A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==7);A=0
	while C+A<len(g)and g[C+A][D]==7:A+=1
	for B in range(A):
		E=D-A+B+1
		for F in range(E,D+A-B):g[C+B][F]=(8,7)[(B+F-E)%2]
	return g