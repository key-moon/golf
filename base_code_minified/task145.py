def p(A):
	G,F=len(A),len(A[0]);from collections import deque;H=[[0]*F for A in A];I=deque()
	for B in range(G):
		for C in range(F):
			if A[B][C]==0 and(B==0 or C==0 or B==G-1 or C==F-1):H[B][C]=1;I.append((B,C))
	while I:
		B,C=I.popleft()
		for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
			D,E=B+J,C+K
			if 0<=D<G and 0<=E<F and A[D][E]==0 and not H[D][E]:H[D][E]=1;I.append((D,E))
	for B in range(G):
		for C in range(F):
			if A[B][C]==0 and not H[B][C]:A[B][C]=1
	for B in range(G):
		for C in range(F):
			if A[B][C]==0:
				for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
					D,E=B+J,C+K
					if 0<=D<G and 0<=E<F and A[D][E]==2:A[B][C]=8;break
	return A