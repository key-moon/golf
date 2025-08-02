def p(A):
	H=len(A);I=len(A[0]);G=[[0]*I for A in range(H)];F=[]
	for B in range(H):
		for C in range(I):
			if A[B][C]==2 and not G[B][C]:
				J=[(B,C)];G[B][C]=1;K=[(B,C)]
				while K:
					M,N=K.pop()
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=M+O,N+P
						if 0<=D<H and 0<=E<I and A[D][E]==2 and not G[D][E]:G[D][E]=1;K.append((D,E));J.append((D,E))
				if len(J)>len(F):F=J
	Q=max(A for(A,B)in enumerate(A)if 1 in B);R=max(A for(A,B)in F);L=Q+1-R
	for(B,C)in F:A[B][C]=0
	for(B,C)in F:
		if A[B+L][C]==0:A[B+L][C]=2
	return A