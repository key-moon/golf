def p(A):
	J=[A[:]for A in A];D,E=len(A),len(A[0]);I=[(B,C)for B in(0,D-1)for C in range(E)if A[B][C]!=5]+[(B,C)for B in range(D)for C in(0,E-1)if A[B][C]!=5];F=set()
	while I:
		B,C=I.pop()
		if(B,C)in F:continue
		F.add((B,C))
		for(K,L)in((1,0),(-1,0),(0,1),(0,-1)):
			G,H=B+K,C+L
			if 0<=G<D and 0<=H<E and A[G][H]!=5 and(G,H)not in F:I.append((G,H))
	for B in range(D):
		for C in range(E):
			if A[B][C]==0 and(B,C)not in F:J[B][C]=4
	return J