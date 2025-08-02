def p(A):
	from collections import Counter as N,deque;D,E=len(A),len(A[0]);M=N(A for B in A for A in B if A).most_common(1)[0][0];L=[[A[B][C]==M for C in range(E)]for B in range(D)];F=[[0]*E for A in range(D)];I=deque()
	for B in range(D):
		for C in(0,E-1):
			if not L[B][C]:F[B][C]=1;I.append((B,C))
	for C in range(E):
		for B in(0,D-1):
			if not L[B][C]and not F[B][C]:F[B][C]=1;I.append((B,C))
	while I:
		G,H=I.popleft()
		for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
			J,K=G+O,H+P
			if 0<=J<D and 0<=K<E and not L[J][K]and not F[J][K]:F[J][K]=1;I.append((J,K))
	for G in range(D):
		for H in range(E):A[G][H]=M if L[G][H]or A[G][H]and not F[G][H]else 0
	return A