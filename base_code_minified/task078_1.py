def p(val_g):
	C=val_g;H=len(C);I=len(C[0]);G=[[0]*I for A in range(H)];F=[]
	for A in range(H):
		for B in range(I):
			if C[A][B]==2 and not G[A][B]:
				J=[(A,B)];G[A][B]=1;K=[(A,B)]
				while K:
					M,N=K.pop()
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=M+O,N+P
						if 0<=D<H and 0<=E<I and C[D][E]==2 and not G[D][E]:G[D][E]=1;K.append((D,E));J.append((D,E))
				if len(J)>len(F):F=J
	Q=max(A for(A,B)in enumerate(C)if 1 in B);R=max(A for(A,B)in F);L=Q+1-R
	for(A,B)in F:C[A][B]=0
	for(A,B)in F:
		if C[A+L][B]==0:C[A+L][B]=2
	return C