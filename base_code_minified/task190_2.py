def p(g):
	A=len(g);E,F=next((B,C)for B in range(A-1)for C in range(A-1)if g[B][C]and g[B][C]==g[B][C+1]==g[B+1][C]==g[B+1][C+1]);G=g[E][F]
	for B in range(A):
		for C in range(A):
			if g[B][C]==G and not(E<=B<=E+1 and F<=C<=F+1):
				H=1 if B>E else-1;I=1 if C>F else-1;D=1
				while 0<=B+D*H<A and 0<=C+D*I<A:g[B+D*H][C+D*I]=G;D+=1
	return g