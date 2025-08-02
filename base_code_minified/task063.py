def p(A):
	K=len(A);L=len(A[0]);F=set();M=[];N=0
	for G in range(K):
		for H in range(L):
			if A[G][H]==0 and(G,H)not in F:
				J=[(G,H)];F.add((G,H));I=[]
				while J:
					B,C=J.pop();I.append((B,C))
					for O in(1,-1):
						for(D,E)in((B+O,C),(B,C+O)):
							if 0<=D<K and 0<=E<L and A[D][E]==0 and(D,E)not in F:F.add((D,E));J.append((D,E))
				if len(I)>N:N,M=len(I),I
	for(B,C)in M:A[B][C]=3
	return A