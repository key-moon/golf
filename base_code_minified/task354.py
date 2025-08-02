def p(A):
	I=set()
	for D in range(len(A)):
		for E in range(len(A[0])):
			if A[D][E]==5 and(D,E)not in I:
				J=[(D,E)];F=[(D,E)];I.add((D,E))
				while J:
					C,B=J.pop()
					for(G,H)in((C+1,B),(C-1,B),(C,B+1),(C,B-1)):
						try:
							if A[G][H]==5 and(G,H)not in I:I.add((G,H));J+=[(G,H)];F+=[(G,H)]
						except:0
				K=min(A for(A,B)in F);L=min(A for(B,A)in F);M=max(A for(B,A)in F)
				for B in range(L,M+1):
					if A[K-1][B]:N=A[K-1][B];break
				for(C,B)in F:A[C][B]=N
	return A