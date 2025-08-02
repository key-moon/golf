def p(g):
	E,F=len(g),len(g[0])
	for G in range(E):
		if any(A==8 for A in g[G]):I=[A for(A,B)in enumerate(g[G])if B==8];J=G;break
	H=[B for A in range(E)for(B,C)in enumerate(g[A])if C==2];K=1 if H and sum(H)/len(H)<F/2 else-1;D=[[0]*F for A in range(E)]
	for A in range(E):
		for(B,L)in enumerate(g[A]):
			if L==2:D[A][B]=2
	C=I[:]
	for A in range(J,E):
		if any(A==2 for A in g[A]):C=[A+K for A in C]
		for B in C:
			if 0<=B<F and D[A][B]==0:D[A][B]=8
	C=I[:]
	for A in range(J-1,-1,-1):
		if any(A==2 for A in g[A]):C=[A+K for A in C]
		for B in C:
			if 0<=B<F and D[A][B]==0:D[A][B]=8
	return D