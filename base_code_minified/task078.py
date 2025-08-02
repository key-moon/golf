def p(g):
	D,E=len(g),len(g[0]);A=[(A,B)for A in range(D)for B in range(E)if g[A][B]==2];F,G=min(A for(A,B)in A),min(A for(B,A)in A);H=[(A-F,B-G)for(A,B)in A]
	for(I,J)in A:g[I][J]=0
	for B in range(D):
		for C in range(E):
			if(B,C)!=(F,G)and all(0<=B+A<D and 0<=C+F<E and g[B+A][C+F]==0 for(A,F)in H):
				for(K,L)in H:g[B+K][C+L]=2
				return g
	return g