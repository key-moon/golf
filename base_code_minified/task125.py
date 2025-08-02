def p(A):
	N=len(A);O=len(A[0]);L=set()
	for D in range(N):
		for E in range(O):
			if A[D][E]==6 and(D,E)not in L:
				M=[(D,E)];L.add((D,E));F=G=D;H=I=E
				while M:
					J,K=M.pop()
					if J<F:F=J
					if K<H:H=K
					if J>G:G=J
					if K>I:I=K
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=J+P,K+Q
						if 0<=B<N and 0<=C<O and A[B][C]==6 and(B,C)not in L:L.add((B,C));M+=[(B,C)]
				F-=1;H-=1;G+=1;I+=1
				for B in range(F,G+1):
					for C in range(H,I+1):
						if B in(F,G)or C in(H,I):A[B][C]=3
						elif A[B][C]!=6:A[B][C]=4
	return A