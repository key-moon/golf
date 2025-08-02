def p(g):
	A={};[A.setdefault(B,[]).append((C,E))for(C,D)in enumerate(g)for(E,B)in enumerate(D)if B];C=[[0]*3 for A in range(3)]
	for D in sorted(A,key=lambda val_c:min(A[val_c])):B=A[D];E=next(A for A in B if sum(abs(A[0]-B[0])+abs(A[1]-B[1])==1 for B in B)==2)
	for(F,G)in B:C[F-E[0]+1][G-E[1]+1]=D
	return C