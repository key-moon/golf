def p(g):
	H,B=len(g),len(g[0]);E=[]
	for F in g:
		A=0
		while A<B:
			C=F[A]
			if C:
				D=A+1
				while D<B and F[D]==C:D+=1
				E+=[(D-A,C)];A=D
			else:A+=1
	E.sort(reverse=1);G=[[0]*B for A in g]
	for(I,(J,C))in enumerate(E):
		for A in range(B-J,B):G[H-1-I][A]=C
	return G