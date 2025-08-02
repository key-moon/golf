def p(A):
	K,L=len(A),len(A[0]);F=set();G=()
	for D in range(K):
		for E in range(L):
			if not A[D][E]and(D,E)not in F:
				M=[(D,E)];H={(D,E)};F.add((D,E))
				for(I,J)in M:
					for(N,O)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=I+N,J+O
						if 0<=B<K and 0<=C<L and not A[B][C]and(B,C)not in F:F.add((B,C));H.add((B,C));M.append((B,C))
				if len(H)>len(G):G=H
	for(I,J)in G:A[I][J]=1
	return A