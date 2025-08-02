def p(g):
	C=set();H=len(g);I=len(g[0]);J=(1,0),(-1,0),(0,1),(0,-1)
	for D in range(H):
		for E in range(I):
			if g[D][E]==4 and(D,E)not in C:
				B=[(D,E)];C.add((D,E))
				for(F,G)in B:
					for(K,L)in J:
						A=F+K,G+L
						if A not in C and 0<=A[0]<H and 0<=A[1]<I and g[A[0]][A[1]]==4:C.add(A);B.append(A)
				M=min(A[0]for A in B);N=max(A[0]for A in B);O=min(A[1]for A in B);P=max(A[1]for A in B)
				for F in range(M,N+1):
					for G in range(O,P+1):
						if g[F][G]==0:g[F][G]=7
	return g