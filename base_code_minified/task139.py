def p(A):
	N,O=len(A),len(A[0]);H=set()
	for F in range(N):
		for G in range(O):
			if A[F][G]==4 and(F,G)not in H:
				I=[(F,G)];H.add((F,G));J=K=F;L=M=G
				while I:
					B,C=I.pop()
					if B<J:J=B
					if B>K:K=B
					if C<L:L=C
					if C>M:M=C
					for(D,E)in((B+1,C),(B-1,C),(B,C+1),(B,C-1)):
						if 0<=D<N and 0<=E<O and A[D][E]==4 and(D,E)not in H:H.add((D,E));I.append((D,E))
				for D in range(J,K+1):
					for E in range(L,M+1):
						if A[D][E]==0:A[D][E]=7
	return A