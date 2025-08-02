def p(A):
	H={};M,N=len(A),len(A[0])
	for D in range(M):
		for E in range(N):
			I=A[D][E]
			if I:
				J=D;K=E;A[D][E]=0;L=[(D,E)]
				while L:
					B,C=L.pop()
					if B<J:J=B
					if C<K:K=C
					for(F,G)in((B+1,C),(B-1,C),(B,C+1),(B,C-1)):
						if 0<=F<M and 0<=G<N and A[F][G]==I:A[F][G]=0;L.append((F,G))
				H.setdefault(J,[]).append((K,I))
	return[[A for(B,A)in sorted(H[A])]for A in sorted(H)]