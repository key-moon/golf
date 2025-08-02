def p(g):
	C=len(g[0]);A=C-1;D=2*A;E=(A-len(g)+1)%D
	for B in range(len(g)):F=abs((B+E)%D-A);g[B]=[8]*C;g[B][F]=1
	return g