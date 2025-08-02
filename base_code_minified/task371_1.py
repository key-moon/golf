def p(g):
	E=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D];(F,G),(H,I)=E;A,B=(F+H)//2,(G+I)//2
	for(C,D)in((A,B),(A-1,B),(A+1,B),(A,B-1),(A,B+1)):
		if 0<=C<len(g)and 0<=D<len(g[0]):g[C][D]=3
	return g