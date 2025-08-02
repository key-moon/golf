def p(g):
	F,E=len(g),len(g[0]);C=[[0]*E for A in g];D=[(A,B)for A in(0,F-1)for B in range(E)if g[A][B]==0]+[(B,A)for A in(0,E-1)for B in range(F)if g[B][A]==0]
	for(A,B)in D:C[A][B]=1
	while D:
		A,B=D.pop()
		if A>0 and not C[A-1][B]and g[A-1][B]==0:C[A-1][B]=1;D.append((A-1,B))
		if A+1<F and not C[A+1][B]and g[A+1][B]==0:C[A+1][B]=1;D.append((A+1,B))
		if B>0 and not C[A][B-1]and g[A][B-1]==0:C[A][B-1]=1;D.append((A,B-1))
		if B+1<E and not C[A][B+1]and g[A][B+1]==0:C[A][B+1]=1;D.append((A,B+1))
	for A in range(F):
		for B in range(E):
			if g[A][B]==0 and not C[A][B]:g[A][B]=4
	return g