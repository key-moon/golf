def p(g):
	A=[A[:]for A in g];E=len(g);F=len(g[0]);G=min(B for C in range(E)for B in range(F)if A[C][B]==2);H=max(B for C in range(E)for B in range(F)if A[C][B]==2);I=set()
	for B in range(E):
		for C in range(F):
			if A[B][C]==8:
				if any(A[B][C]==2 for C in range(C)):
					J=max(C for C in range(C)if A[B][C]==2);I.add(G)
					for D in range(J+1,C):g[B][D]=8
				else:
					J=min(C for C in range(C+1,F)if A[B][C]==2);I.add(H)
					for D in range(C+1,J):g[B][D]=8
				g[B][C]=4
	for K in(G,H):
		if K not in I:
			L=[B for B in range(E)if A[B][K]==2];M=(min(L)+max(L))//2
			if K==G:
				for D in range(G+1,H):g[M][D]=8
			else:
				for D in range(H):g[M][D]=8
	return g